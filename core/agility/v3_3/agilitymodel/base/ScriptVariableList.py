from ServiceMeshList import ServiceMeshListBase

class ScriptVariableListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, scriptvariable=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'scriptVariable': {'maxOccurs': 'unbounded', 'type': 'ScriptVariable', 'name': 'scriptvariable', 'minOccurs': '0', 'native': False}})
        self.scriptvariable = scriptvariable 
