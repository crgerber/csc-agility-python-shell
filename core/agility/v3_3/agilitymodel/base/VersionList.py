from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class VersionListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, versions=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'versions': {'maxOccurs': 'unbounded', 'native': False, 'name': 'versions', 'minOccurs': '0', 'type': 'AgilityVersion'}})
        self.versions = versions 
