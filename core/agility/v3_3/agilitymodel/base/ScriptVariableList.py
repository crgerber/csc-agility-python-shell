from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class ScriptVariableListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, scriptvariable=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'scriptVariable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'scriptvariable', 'minOccurs': '0', 'type': 'ScriptVariable'}})
        self.scriptvariable = scriptvariable 
