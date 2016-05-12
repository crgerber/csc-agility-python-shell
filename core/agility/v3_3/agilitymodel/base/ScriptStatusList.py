from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class ScriptStatusListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, scriptstatus=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'scriptStatus': {'maxOccurs': 'unbounded', 'native': False, 'name': 'scriptstatus', 'minOccurs': '0', 'type': 'ScriptStatus'}})
        self.scriptstatus = scriptstatus 