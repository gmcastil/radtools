import pandas as pd
import pandas.util.testing as pdt
import numpy.testing as npt

import crosssection

DATA = "./tests/data/cross-sections.dat"
HEADER = ["LET", "fluence", "events",  "cross section",
          "lower limit", "upper limit"]
RTOL = 0.1

class Parent():
    """Class for subclassing different datasets - do not invoke directly"""

    def test_cross_section(self):
        events = self.data["events"].values
        fluence = self.data["fluence"].values

        result = crosssection.cross_section(events, fluence)
        right = result["cross section"]
        left = self.data["cross section"].values
        npt.assert_allclose(left, right, rtol=RTOL)

    def test_stats(self):
        events = self.data["events"].values
        fluence = self.data["fluence"].values

        result = crosssection.cross_section(events, fluence)
        right = result["lower limit"]
        left = self.data["lower limit"].values
        npt.assert_allclose(left, right, rtol=RTOL)

        right = result["upper limit"]
        left = self.data["upper limit"].values
        npt.assert_allclose(left, right, rtol=RTOL)

class TestComplete(Parent):
    """Tests cross section with no upper bounds"""

    def setup(self):
        self.data = pd.read_table(DATA, sep="\\s*", comment="#", skiprows=8,
                                  nrows=11, names=HEADER, header=None,
                                  engine="python")

class TestMultiIncomplete(Parent):
    """Tests cross section with more than one upper bounds"""

    def setup(self):
        self.data = pd.read_table(DATA, sep="\\s*", comment="#", skiprows=20,
                                  nrows=9, names=HEADER, header=None,
                                  engine="python")

class TestIncomplete(Parent):
    """Tests cross section with a single upper bound"""

    def setup(self):
        self.data = pd.read_table(DATA, sep="\\s*", comment="#", skiprows=30,
                                  nrows=7, names=HEADER, header=None,
                                  engine="python")
