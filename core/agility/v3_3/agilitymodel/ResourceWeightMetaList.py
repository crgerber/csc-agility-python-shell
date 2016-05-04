from core.agility.v3_3.agilitymodel.base.ResourceWeightMetaList import ResourceWeightMetaListBase
from core.agility.v3_3.agilitymodel.actions.ResourceWeightMetaList import ResourceWeightMetaListActions

class ResourceWeightMetaList(ResourceWeightMetaListBase, ResourceWeightMetaListActions):
    '''
    classdocs
    '''
    def __init__(self, resourceweightmeta=[]):
        '''
        Constructor
        @param resourceweightmeta: resourceweightmeta minOccurs=0 maxOccurs=unbounded
        @type resourceweightmeta: ResourceWeightMeta
        '''
        ResourceWeightMetaListBase.__init__(self, resourceweightmeta=resourceweightmeta)
