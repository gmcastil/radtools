# pylint: disable=C0103

"""
Provides tools for generating SEE cross sections from accelerator testing

Notes:

  * Intended to be called with a dict containing the name of the cross section
    (e.g., 'SEFI') to be found, fluence, events, and LET.
  * Returns dict containing cross section, LET, lower and upper statistical
    limits.

"""
from __future__ import division
from collections import namedtuple
from itertools import izip
from math import sqrt

import numpy as np
from sandia import STAT_DATA

Limits = namedtuple("Limits", ["lower", "upper"], verbose=False)

def cross_section(events, fluence):
    """Builds cross section results from input data

    Args:
      events (arraylike): Number of events observed
      fluence (arraylike): Fluence for each observable

    Returns:
      dict - Cross section, lower, and upper statistical limits

    The order of elements in the return data corresponds to the order
    of the elements in both arguments.

    Raises:
      ValueError - If `events` and `fluence` are not the same length

    """
    if len(events) != len(fluence):
        raise ValueError("Arguments must be the same length")

    lower = []
    upper = []
    result = []
    for num, total_fluence in izip(events, fluence):
        if num == 0:
            x_sect = 1 / total_fluence
        else:
            x_sect = num / total_fluence
        result.append(x_sect)
        stats = _stats(num)
        lower.append(stats.lower*x_sect)
        upper.append(stats.upper*x_sect)


    return {"cross section" : np.asarray(result),
            "lower limit" : np.asarray(lower),
            "upper limit" : np.asarray(upper)}

def _stats(events):
    """Calculate 95% confidence intervals for small numbers of events

    Args:
      events (integer): Number of observables

    Returns
      tuple

    """
    if events < 50:
        lower, upper = STAT_DATA[events]
    else:
        lower = 1 - 2 / sqrt(events)
        upper = 1 + 2 / sqrt(events)

    return Limits(lower, upper)
