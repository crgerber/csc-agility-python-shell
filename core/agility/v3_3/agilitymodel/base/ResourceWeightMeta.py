from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceWeightMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, resourceweightinfo=[], displayname='', id=None, jaxbtype='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceWeightInfo': {'maxOccurs': 'unbounded', 'type': 'ResourceWeightInfo', 'name': 'resourceweightinfo', 'minOccurs': '0', 'native': False}, 'displayName': {'type': 'string', 'name': 'displayname', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'jaxbType': {'type': 'string', 'name': 'jaxbtype', 'native': True}})
        self.resourceweightinfo = resourceweightinfo
        self.displayname = displayname
        self.id = id
        self.jaxbtype = jaxbtype
        self.name = name 
