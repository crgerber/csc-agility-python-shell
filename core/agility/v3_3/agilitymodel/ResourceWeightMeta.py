from core.agility.v3_3.agilitymodel.base.ResourceWeightMeta import ResourceWeightMetaBase
from core.agility.v3_3.agilitymodel.actions.ResourceWeightMeta import ResourceWeightMetaActions

class ResourceWeightMeta(ResourceWeightMetaBase, ResourceWeightMetaActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', displayname='', resourceweightinfo=[], jaxbtype=''):
        '''
        Constructor
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        @param displayname: displayname
        @type displayname: string
        @param resourceweightinfo: resourceweightinfo minOccurs=0 maxOccurs=unbounded
        @type resourceweightinfo: ResourceWeightInfo
        @param jaxbtype: jaxbtype
        @type jaxbtype: string
        '''
        ResourceWeightMetaBase.__init__(self, id=id, name=name, displayname=displayname, resourceweightinfo=resourceweightinfo, jaxbtype=jaxbtype)
