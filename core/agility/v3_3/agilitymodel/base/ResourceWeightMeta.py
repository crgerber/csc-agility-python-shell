from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceWeightMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, resourceweightinfo=[], name='', displayname='', jaxbtype='', id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'type': 'string'}, 'resourceWeightInfo': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resourceweightinfo', 'minOccurs': '0', 'type': 'ResourceWeightInfo'}, 'displayName': {'native': True, 'name': 'displayname', 'type': 'string'}, 'jaxbType': {'native': True, 'name': 'jaxbtype', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}})
        self.resourceweightinfo = resourceweightinfo
        self.name = name
        self.displayname = displayname
        self.jaxbtype = jaxbtype
        self.id = id 
