from ..errors import DataSizeError
from ..tools import Data


class Averages:
    """
    Attempting not to re-invent the wheel.
    The methods below already exist under the statistics model in 3.5
    """
    def __init__(self, data):
        self.data = Data(data)

    def median(self):
        pass

    def mean(self):
        pass

    def mode(self):
        pass


class Spread:
    def __init__(self, **kwargs):
        pass

    def range(self):
        pass

    def quartiles(self):
        pass

    def variance(self):
        pass

    def standard_deviation(self):
        pass


class Quartiles:
    def __init__(self, **kwargs):
        pass

    def quartiles(self):
        pass

    def interquartiles(self):
        pass

