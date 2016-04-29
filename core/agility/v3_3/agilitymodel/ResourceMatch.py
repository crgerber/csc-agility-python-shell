from core.agility.v3_3.agilitymodel.base.ResourceMatch import ResourceMatchBase
from core.agility.v3_3.agilitymodel.actions.ResourceMatch import ResourceMatchActions

class ResourceMatch(ResourceMatchBase, ResourceMatchActions):
    '''
    classdocs
    '''
    def __init__(self, metric=[], rank=None, stackdefault=False):
        '''
        Constructor
        @param metric: metric minOccurs=0 maxOccurs=unbounded
        @type metric: ResourceMetric
        @param rank: rank
        @type rank: double
        @param stackdefault: stackdefault
        @type stackdefault: boolean
        '''
        ResourceMatchBase.__init__(self, metric=metric, rank=rank, stackdefault=stackdefault)
