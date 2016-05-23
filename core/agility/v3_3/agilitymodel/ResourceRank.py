from core.agility.v3_3.agilitymodel.base.ResourceRank import ResourceRankBase
from core.agility.v3_3.agilitymodel.actions.ResourceRank import ResourceRankActions

class ResourceRank(ResourceRankBase, ResourceRankActions):
    '''
    classdocs
    '''
    def __init__(self, name=None, weight=[], type=''):
        '''
        Constructor
        @param name: name minOccurs=0
        @type name: string
        @param weight: weight minOccurs=0 maxOccurs=unbounded
        @type weight: ResourceWeight
        @param type: type
        @type type: string
        '''
        ResourceRankBase.__init__(self, name=name, weight=weight, type=type)
