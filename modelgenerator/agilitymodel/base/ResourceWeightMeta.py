from AgilityModelBase import AgilityModelBase

class ResourceWeightMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, resourceWeightInfo=list(), displayName='', id=None, jaxbType='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceWeightInfo': {'maxOccurs': 'unbounded', 'type': 'ResourceWeightInfo', 'name': 'resourceWeightInfo', 'minOccurs': '0', 'native': False}, 'displayName': {'type': 'string', 'name': 'displayName', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'jaxbType': {'type': 'string', 'name': 'jaxbType', 'native': True}})
        self.resourceWeightInfo = resourceWeightInfo
        self.displayName = displayName
        self.id = id
        self.jaxbType = jaxbType
        self.name = name 
