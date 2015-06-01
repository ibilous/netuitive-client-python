
class Metric(object):

    """A performance measure that is associated with Element

    Args:
        metricId: The name of the metric
        metricType: The type of the metric

    """

    def __init__(self, metricId, metricType=None):
        self.id = metricId
        self.type = metricType