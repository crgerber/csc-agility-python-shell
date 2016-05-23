from core.agility.v3_3.agilitymodel.base.ResourceMapping import ResourceMappingBase
from core.agility.v3_3.agilitymodel.actions.ResourceMapping import ResourceMappingActions

class ResourceMapping(ResourceMappingBase, ResourceMappingActions):
    '''
    classdocs
    '''
    def __init__(self, description=None, rank=[], condition=None, name=None, exclusion=None, inclusion=None):
        '''
        Constructor
        @param description: description minOccurs=0
        @type description: string
        @param rank: rank minOccurs=0 maxOccurs=unbounded
        @type rank: ResourceRank
        @param condition: condition minOccurs=0
        @type condition: AssetFilter
        @param name: name minOccurs=0
        @type name: string
        @param exclusion: exclusion minOccurs=0
        @type exclusion: AssetFilter
        @param inclusion: inclusion minOccurs=0
        @type inclusion: AssetFilter
        '''
        ResourceMappingBase.__init__(self, description=description, rank=rank, condition=condition, name=name, exclusion=exclusion, inclusion=inclusion)
