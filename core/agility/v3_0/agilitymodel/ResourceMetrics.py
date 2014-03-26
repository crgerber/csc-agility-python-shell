from core.agility.v3_0.agilitymodel.base.ResourceMetrics import ResourceMetricsBase
from core.agility.v3_0.agilitymodel.actions.ResourceMetrics import ResourceMetricsActions

class ResourceMetrics(ResourceMetricsBase, ResourceMetricsActions):
    '''
    classdocs
    '''
    def __init__(self, metric=[]):
        '''
        Constructor
        @param metric: metric minOccurs=0 maxOccurs=unbounded
        @type metric: ResourceMetric
        '''
        ResourceMetricsBase.__init__(self, metric=metric)
