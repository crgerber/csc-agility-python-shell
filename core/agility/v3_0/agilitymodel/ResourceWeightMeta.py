from core.agility.v3_0.agilitymodel.base.ResourceWeightMeta import ResourceWeightMetaBase
from core.agility.v3_0.agilitymodel.actions.ResourceWeightMeta import ResourceWeightMetaActions

class ResourceWeightMeta(ResourceWeightMetaBase, ResourceWeightMetaActions):
    '''
    classdocs
    '''
    def __init__(self, resourceweightinfo=[], displayname='', id=None, jaxbtype='', name=''):
        '''
        Constructor
        @param resourceweightinfo: resourceweightinfo minOccurs=0 maxOccurs=unbounded
        @type resourceweightinfo: ResourceWeightInfo
        @param displayname: displayname
        @type displayname: string
        @param id: id
        @type id: int
        @param jaxbtype: jaxbtype
        @type jaxbtype: string
        @param name: name
        @type name: string
        '''
        ResourceWeightMetaBase.__init__(self, resourceweightinfo=resourceweightinfo, displayname=displayname, id=id, jaxbtype=jaxbtype, name=name)
