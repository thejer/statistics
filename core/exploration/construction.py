import inspect
import random

import numpy

from core import tools
from core.tools import Data
import matplotlib.pyplot as stats_plot


class Construction:
    def __init__(self, data=None, **kwargs):
        '''
        Constructing and interpreting graphical displays of distributions of
        univariate data (dotplot, stemplot, histogram, cumulative frequency plot)
        1. Center and spread
        2. Clusters and gaps
        3. Outliers and other unusual features
        4. Shape
        '''
        if kwargs.get('random_data'):
            self.data = Data(tools.generate_random_data(kwargs.get('length'), kwargs.get('data_range')))
        self.data = Data(data)
        # stats_plot.title(kwargs.get('title'), inspect.stack()[1][3])
        # stats_plot.xlabel(kwargs.get('x_label'))
        # stats_plot.ylabel(kwargs.get('y_label'))

    def dot_plot(self, axis=None, color="ro", **kwargs):
        stats_plot.plot(self.data.to_list())
        plot = stats_plot.axis(axis)
        if not kwargs.get('show'):
            self._save_fig(kwargs.get('fig_name'))
        else:
            self._show_fig(plot)

    def basic_histogram(self,**kwargs):
        """
        https://plot.ly/matplotlib/histograms/
        :return: 
        """
        histogram = stats_plot.hist(self.data.to_list())
        if not kwargs.get('show'):
            self._save_fig(kwargs.get('fig_name'))
        else:
            self._show_fig(histogram)


    def combined_histogram(self, *data_sets, **kwargs):
        """
        
        :return: 
        """
        histogram = stats_plot.hist(*data_sets)
        if not kwargs.get('show'):
            self._save_fig(kwargs.get('fig_name'))
        else:
            self._show_fig(histogram)

    def mutiple_dataset_histogram(self):
        """
        
        :return: 
        """
        pass

    def _show_fig(self, plot):
        stats_plot.show(plot)

    def _save_fig(self, fig_name):
        stats_plot.savefig('{0}.png'.format(fig_name))

# test = Construction(random.sample(range(10000), 5))
# y = [5,6,7,2,4,6,]
# set_d = [[1, 2, 3,4,5], y, range(10)]
# test.combined_history(set_d)

# import random
# import numpy
# import matplotlib.pyplot as plt
#
# histogram=plt.figure()
#
# x = [random.gauss(3,1) for _ in range(400)]
# y = [random.gauss(4,2) for _ in range(400)]
#
# plt.hist(x)
# plt.hist(y)
# plt.show()
