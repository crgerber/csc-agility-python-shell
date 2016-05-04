from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class VariableListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, variable=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variable': {'maxOccurs': 'unbounded', 'type': 'Variable', 'name': 'variable', 'minOccurs': '0', 'native': False}})
        self.variable = variable 
