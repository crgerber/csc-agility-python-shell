from ServiceMeshList import ServiceMeshListBase

class PropertyDefinitionListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, definition=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'definition': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'definition', 'minOccurs': '0', 'native': False}})
        self.definition = definition 
