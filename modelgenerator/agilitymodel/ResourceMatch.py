from base.ResourceMatch import ResourceMatchBase
from actions.ResourceMatch import ResourceMatchActions

class ResourceMatch(ResourceMatchBase, ResourceMatchActions):
    '''
    classdocs
    '''
    def __init__(self, metric=list(), rank=None):
        '''
        Constructor
        @param metric: metric minOccurs=0 maxOccurs=unbounded
        @type metric: ResourceMetric
        @param rank: rank
        @type rank: double
        '''
        ResourceMatchBase.__init__(self, metric=metric, rank=rank)
