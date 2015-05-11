"""
Defines values to be used in calculating upper and lower statistical limits

In order to calculate upper and lower limits for values of N < 50, compute the
cross section in the usual way, then find the corresponding pair of values for
N and multiply the cross section by each to yield the lower and upper limits.
For N >= 50, the upper and lower limits can be found simply by multiplying by
(1 +/- 2/\\sqrt(N)) respectively.

Note that these are absolute values and additional processing may be necessary
depending upon the plotting package.

.. [1] J. Schwank, "Radiation hardness assurance testing of microelectronic
       devices and integrated circuits: test guideline for proton and heavy ion
       single-event effects", Sandia National Laboratories Document
       Sand 2008-6983P, 2008.

"""

STAT_DATA = {0 : (0.000, 3.700),
             1 : (0.100, 5.600),
             2 : (0.100, 3.600),
             3 : (0.200, 2.933),
             4 : (0.250, 2.550),
             5 : (0.320, 2.340),
             6 : (0.367, 2.183),
             7 : (0.400, 2.057),
             8 : (0.425, 1.975),
             9 : (0.444, 1.900),
             10 : (0.470, 1.840),
             11 : (0.491, 1.791),
             12 : (0.517, 1.750),
             13 : (0.531, 1.715),
             14 : (0.550, 1.679),
             15 : (0.560, 1.653),
             16 : (0.588, 1.625),
             17 : (0.582, 1.600),
             18 : (0.594, 1.578),
             19 : (0.605, 1.558),
             20 : (0.610, 1.540),
             21 : (0.619, 1.524),
             22 : (0.627, 1.509),
             23 : (0.635, 1.496),
             24 : (0.642, 1.483),
             25 : (0.648, 1.47),
             26 : (0.654, 1.46),
             27 : (0.659, 1.45),
             28 : (0.664, 1.44),
             29 : (0.669, 1.43),
             30 : (0.673, 1.42),
             31 : (0.677, 1.41),
             32 : (0.681, 1.40),
             33 : (0.688, 1.40),
             34 : (0.691, 1.39),
             35 : (0.694, 1.39),
             36 : (0.697, 1.38),
             37 : (0.703, 1.37),
             38 : (0.705, 1.37),
             39 : (0.710, 1.36),
             40 : (0.715, 1.36),
             41 : (0.717, 1.35),
             42 : (0.721, 1.35),
             43 : (0.723, 1.34),
             44 : (0.727, 1.34),
             45 : (0.729, 1.33),
             46 : (0.730, 1.33),
             47 : (0.734, 1.33),
             48 : (0.735, 1.32),
             49 : (0.737, 1.32),
             50 : (0.740, 1.31)}