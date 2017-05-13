from ..errors import DataSizeError
from ..tools import Data
import statistics


class Averages:
    """
    Attempting not to re-invent the wheel.
    The methods below already exist under 
    the statistics module in 3.5, So i just called them.
    Would eventually have to rewrite them though.
    """
    def __init__(self,data=None):
        self.data = Data(data)

    def median(self,data=None, data_type=None, **kwargs):
        if not data_type:
            return statistics.median(data)
        elif data_type == 'low':
            return statistics.median_low(data)
        elif data_type == 'high':
            return statistics.median_high(data)
        else:
            return statistics.median_grouped(kwargs.get('interval', 1))

    def mean(self,data=None):
        return statistics.mean(data)

    def mode(self,data=None):
        return statistics.mode(data)


class Spread:
    def __init__(self, **kwargs):
        pass

    def range(self,data=None):
        return max(data) - min(data)

    def variance(self,data=None):
        pass

    def standard_deviation(self,data=None):
        pass

    def population_variance(self,data=None):
        pass


class Quartiles:
    def __init__(self, **kwargs):
        pass

    def quartiles(self,data=None):
        pass

    def interquartiles(self,data=None):
        pass


average = Averages()
spread = Spread()
quartiles = Quartiles()
mean, mode, median = average.mean(), average.mode(), average.median()
spread_range, variance, standard_deviation, population_variance = spread.range(), spread.variance()\
                                                                ,spread.standard_deviation(), spread.population_variance()
quartiles, interquartiles = quartiles.quartiles(), quartiles.interquartiles()
