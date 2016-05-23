from core.agility.v3_3.agilitymodel.base.ResourceMatch import ResourceMatchBase
from core.agility.v3_3.agilitymodel.actions.ResourceMatch import ResourceMatchActions

class ResourceMatch(ResourceMatchBase, ResourceMatchActions):
    '''
    classdocs
    '''
    def __init__(self, rank=None, stackdefault=False, metric=[]):
        '''
        Constructor
        @param rank: rank
        @type rank: double
        @param stackdefault: stackdefault
        @type stackdefault: boolean
        @param metric: metric minOccurs=0 maxOccurs=unbounded
        @type metric: ResourceMetric
        '''
        ResourceMatchBase.__init__(self, rank=rank, stackdefault=stackdefault, metric=metric)
