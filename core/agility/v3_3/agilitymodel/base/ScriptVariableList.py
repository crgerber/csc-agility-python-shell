from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class ScriptVariableListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, scriptvariable=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'scriptVariable': {'name': 'scriptvariable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ScriptVariable'}})
        self.scriptvariable = scriptvariable 
