from .errors import DataSizeError

class Data:
    def __init__(self, data):
        self.data = sorted(data) if data else None
        self.is_discrete = True if self.discrete() else False

    def __repr__(self):
        return '{}'.format(self.data)

    def __str__(self):
        return '{}'.format(self.data)

    def discrete(self):
        return True if isinstance(self.data, dict) else False

    def to_list(self):
        return list(self.data)


def generate_random_data(length, data_range):
    import random
    try:
        return random.sample(range(data_range), length)
    except ValueError:
        raise DataSizeError('Sample data range  is larger than specified length')
