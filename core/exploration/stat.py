class MyAverages:
    """With there being a statistics library in python 3.5
    I decided to add the class I'd written before finding
    out that stat lib already exists"""
    def __init__(self, data=None):
        self.data = data
        self.occ = None
        self.md = None

    def mean(self, data):
        return sum(data) / (len(data))

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

    def variance(self, data):
        self.new_data = []
        for i in self.data:
            self.new_data.append((i - sum(data) / (len(data))) ** 2)
        return sum(self.new_data) / (len(self.new_data))

    def standard_dev(self, data):
        self.new_data = []
        for i in data:
            self.new_data.append((i - (sum(data) / (len(data)))) ** 2)
        return (sum(self.new_data) / len(self.new_data)) ** 0.5

    def range(self, data=None):
        return max(data) - min(data)

average = MyAverages()
spread = MySpread()

mean, median, mode = average.mean(), average.median(), average.mode()
variance, standard_dev, spread_range = spread.variance(), spread.standard_dev(), spread.range()
