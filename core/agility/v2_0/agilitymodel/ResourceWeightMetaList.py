from core.agility.v2_0.agilitymodel.base.ResourceWeightMetaList import ResourceWeightMetaListBase
from core.agility.v2_0.agilitymodel.actions.ResourceWeightMetaList import ResourceWeightMetaListActions

class ResourceWeightMetaList(ResourceWeightMetaListBase, ResourceWeightMetaListActions):
    '''
    classdocs
    '''
    def __init__(self, resourceWeightMeta=list()):
        '''
        Constructor
        @param resourceWeightMeta: resourceWeightMeta minOccurs=0 maxOccurs=unbounded
        @type resourceWeightMeta: ResourceWeightMeta
        '''
        ResourceWeightMetaListBase.__init__(self, resourceWeightMeta=resourceWeightMeta)
