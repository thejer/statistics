class Theory:
    @staticmethod
    def stat_def():
        definition = """Statistics is concerned with scientific methods for collecting, organizing, summarizing, presenting,
        and analyzing data as well as with drawing valid conclusions and making reasonable decisions on the
        basis of such analysis.
        In a narrower sense, the term statistics is used to denote the data themselves or numbers derived
        from the data, such as averages. Thus we speak of employment statistics, accident statistics, etc."""
        return definition

    @staticmethod
    def rel_mean_median_mode():
        relation = "mean - mode = 3(mean - median)"
        return relation

    @staticmethod
    def rel_mean_deviation_standard_deviation():
        relation = "Mean deviation = (4/5) Standard deviation"
        return relation


class MyAverages:
    """With there being a statistics library in python 3.5
    I decided to add the class I'd written before finding
    out that stat lib already exists"""
    def __init__(self, data=None):
        self.data = data
        self.occ = None
        self.md = None

    @staticmethod
    def product(lis):
        p = 1
        for i in lis:
            p *= i
        return p

    def mean(self, data):
        return sum(data) / (len(data))

    def geometric_mean(self, data):
        n = len(data)
        gm = (self.product(data))**(1/n)
        return gm

    def harmonic_mean(self, data):
        lis = [1/i for i in data]
        hm = (len(data)/(sum(lis)))
        return hm

    def root_mean_square(self, data):
        lis = [x**2 for x in data]
        return ((sum(lis))/len(lis))**0.5

    def median(self, data):
        self.data.sort()
        if len(data) % 2 == 0:
            return data[round(((len(data) / 2) + ((len(data) / 2) - 1)) / 2)]
        else:
            return data[(round(len(data) / 2)) - 1]

    def mode(self, data):
        self.occ = 0
        self.md = 0
        for n in self.data:
            if self.occ < data.count(n):
                self.occ = data.count(n)
                self.md = n
        return self.md


class MySpread:

    def __init__(self, data=None):
        self.data = data
        self.new_data = None

    def mean_deviation(self, data):
        lis = [abs(i - (sum(data) / len(data))) for i in data]
        return sum(lis)/len(lis)

    def variance(self, data):
        self.new_data = [(i - sum(data) / (len(data))) ** 2 for i in data]
        return sum(self.new_data) / (len(self.new_data))

    def standard_dev(self, data):
        self.new_data = [(i - (sum(data) / len(data)) ** 2) for i in data]
        return (sum(self.new_data) / len(self.new_data)) ** 0.5

    def range(self, data=None):
        return max(data) - min(data)


class Moments:
    """
    'r' represents the rth moment about the origin '0', the mean, and an arbitrary origin 'a'
    """
    def __init__(self, data=None):
        self.r = None
        self.data = data

    def moment_origin(self, data, r):
        if r == 1:
            return sum(data) / (len(data))
        else:
            lis = [(i**r) for i in data]
            return sum(lis)/len(lis)

    def moment_mean(self, data, r):
        if r == 1:
            return 0
        # elif r == 2:
        #     lis = [(i - sum(data) / (len(data))) ** 2 for i in data]
        #     return sum(lis) / (len(lis))
        else:
            lis = [(i - (sum(data) / (len(data))))**r for i in data]
            return sum(lis)/len(lis)

    def moment_arbitrary_origin(self, data, r, a):
        lis = [(i - a)**r for i in data]
        return sum(lis)/len(lis)

average = MyAverages()
spread = MySpread()

mean, median, mode = average.mean(), average.median(), average.mode()
variance, standard_dev, spread_range = spread.variance(), spread.standard_dev(), spread.range()
