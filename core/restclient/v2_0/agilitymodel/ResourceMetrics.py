from core.restclient.v2_0.agilitymodel.base.ResourceMetrics import ResourceMetricsBase
from core.restclient.v2_0.agilitymodel.actions.ResourceMetrics import ResourceMetricsActions

class ResourceMetrics(ResourceMetricsBase, ResourceMetricsActions):
    '''
    classdocs
    '''
    def __init__(self, metric=list()):
        '''
        Constructor
        @param metric: metric minOccurs=0 maxOccurs=unbounded
        @type metric: ResourceMetric
        '''
        ResourceMetricsBase.__init__(self, metric=metric)
