from base.ResourceWeightMetaList import ResourceWeightMetaListBase
from actions.ResourceWeightMetaList import ResourceWeightMetaListActions

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
