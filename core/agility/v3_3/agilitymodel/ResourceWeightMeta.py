from core.agility.v3_3.agilitymodel.base.ResourceWeightMeta import ResourceWeightMetaBase
from core.agility.v3_3.agilitymodel.actions.ResourceWeightMeta import ResourceWeightMetaActions

class ResourceWeightMeta(ResourceWeightMetaBase, ResourceWeightMetaActions):
    '''
    classdocs
    '''
    def __init__(self, resourceweightinfo=[], name='', displayname='', jaxbtype='', id=None):
        '''
        Constructor
        @param resourceweightinfo: resourceweightinfo minOccurs=0 maxOccurs=unbounded
        @type resourceweightinfo: ResourceWeightInfo
        @param name: name
        @type name: string
        @param displayname: displayname
        @type displayname: string
        @param jaxbtype: jaxbtype
        @type jaxbtype: string
        @param id: id
        @type id: int
        '''
        ResourceWeightMetaBase.__init__(self, resourceweightinfo=resourceweightinfo, name=name, displayname=displayname, jaxbtype=jaxbtype, id=id)