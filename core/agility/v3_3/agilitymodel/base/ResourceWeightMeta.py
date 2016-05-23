from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceWeightMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', displayname='', resourceweightinfo=[], jaxbtype=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'displayName': {'name': 'displayname', 'native': True, 'type': 'string'}, 'resourceWeightInfo': {'name': 'resourceweightinfo', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ResourceWeightInfo'}, 'jaxbType': {'name': 'jaxbtype', 'native': True, 'type': 'string'}})
        self.id = id
        self.name = name
        self.displayname = displayname
        self.resourceweightinfo = resourceweightinfo
        self.jaxbtype = jaxbtype 
