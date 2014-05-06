from core.agility.v2_0.agilitymodel.base.ResourceWeightMeta import ResourceWeightMetaBase
from core.agility.v2_0.agilitymodel.actions.ResourceWeightMeta import ResourceWeightMetaActions

class ResourceWeightMeta(ResourceWeightMetaBase, ResourceWeightMetaActions):
    '''
    classdocs
    '''
    def __init__(self, resourceWeightInfo=list(), displayName='', id=None, jaxbType='', name=''):
        '''
        Constructor
        @param resourceWeightInfo: resourceWeightInfo minOccurs=0 maxOccurs=unbounded
        @type resourceWeightInfo: ResourceWeightInfo
        @param displayName: displayName
        @type displayName: string
        @param id: id
        @type id: int
        @param jaxbType: jaxbType
        @type jaxbType: string
        @param name: name
        @type name: string
        '''
        ResourceWeightMetaBase.__init__(self, resourceWeightInfo=resourceWeightInfo, displayName=displayName, id=id, jaxbType=jaxbType, name=name)
