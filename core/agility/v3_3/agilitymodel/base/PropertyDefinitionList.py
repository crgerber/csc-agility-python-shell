from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class PropertyDefinitionListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, definition=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'definition': {'name': 'definition', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyDefinition'}})
        self.definition = definition 
