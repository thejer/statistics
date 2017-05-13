class StatsError(Exception):
    def __init__(self, message):
        pass


class DataSizeError(StatsError):
    def __init__(self, message):
        super(StatsError, self).__init__(message)
        pass
