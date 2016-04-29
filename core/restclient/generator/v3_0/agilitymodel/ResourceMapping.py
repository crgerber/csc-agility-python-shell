from .base.ResourceMapping import ResourceMappingBase
from .actions.ResourceMapping import ResourceMappingActions

class ResourceMapping(ResourceMappingBase, ResourceMappingActions):
    '''
    classdocs
    '''
    def __init__(self, exclusion=None, inclusion=None, description=None, rank=[], condition=None, name=None):
        '''
        Constructor
        @param exclusion: exclusion minOccurs=0
        @type exclusion: AssetFilter
        @param inclusion: inclusion minOccurs=0
        @type inclusion: AssetFilter
        @param description: description minOccurs=0
        @type description: string
        @param rank: rank minOccurs=0 maxOccurs=unbounded
        @type rank: ResourceRank
        @param condition: condition minOccurs=0
        @type condition: AssetFilter
        @param name: name minOccurs=0
        @type name: string
        '''
        ResourceMappingBase.__init__(self, exclusion=exclusion, inclusion=inclusion, description=description, rank=rank, condition=condition, name=name)
