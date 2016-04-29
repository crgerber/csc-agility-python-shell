from .base.ResourceRank import ResourceRankBase
from .actions.ResourceRank import ResourceRankActions

class ResourceRank(ResourceRankBase, ResourceRankActions):
    '''
    classdocs
    '''
    def __init__(self, type='', name=None, weight=[]):
        '''
        Constructor
        @param type: type
        @type type: string
        @param name: name minOccurs=0
        @type name: string
        @param weight: weight minOccurs=0 maxOccurs=unbounded
        @type weight: ResourceWeight
        '''
        ResourceRankBase.__init__(self, type=type, name=name, weight=weight)
