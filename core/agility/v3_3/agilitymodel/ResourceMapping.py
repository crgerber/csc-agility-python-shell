from core.agility.v3_3.agilitymodel.base.ResourceMapping import ResourceMappingBase
from core.agility.v3_3.agilitymodel.actions.ResourceMapping import ResourceMappingActions

class ResourceMapping(ResourceMappingBase, ResourceMappingActions):
    '''
    classdocs
    '''
    def __init__(self, condition=None, exclusion=None, description=None, name=None, rank=[], inclusion=None):
        '''
        Constructor
        @param condition: condition minOccurs=0
        @type condition: AssetFilter
        @param exclusion: exclusion minOccurs=0
        @type exclusion: AssetFilter
        @param description: description minOccurs=0
        @type description: string
        @param name: name minOccurs=0
        @type name: string
        @param rank: rank minOccurs=0 maxOccurs=unbounded
        @type rank: ResourceRank
        @param inclusion: inclusion minOccurs=0
        @type inclusion: AssetFilter
        '''
        ResourceMappingBase.__init__(self, condition=condition, exclusion=exclusion, description=description, name=name, rank=rank, inclusion=inclusion)
