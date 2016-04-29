from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class InputVariableListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, inputvariable=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'inputVariable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'inputvariable', 'minOccurs': '0', 'type': 'InputVariable'}})
        self.inputvariable = inputvariable 
