"""
Provides tools for generating SEE cross sections from accelerator testing

Notes:

  * Intended to be called with a dict containing the name of the cross section
    (e.g., 'SEFI') to be found, fluence, events, and LET.
  * Returns dict containing cross section, LET, lower and upper statistical
    limits.

"""
from collections import namedtuple
from sandia import STAT_DATA

Limits = namedtuple("Limits", ["lower", "upper"], verbose=False)

def cross_section(data):
    """Builds cross section results from input data

    Args:
      data (dict): Type, fluence, events, and LET

    Returns:
      dict

    """

def stats(events):
    """Calculates 95% confidence intervals for small numbers of events

    Args:
      events (integer): Number of observables

    Returns
      tuple

    """

