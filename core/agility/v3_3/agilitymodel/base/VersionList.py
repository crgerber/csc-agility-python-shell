from ServiceMeshList import ServiceMeshListBase

class VersionListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, versions=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'versions': {'maxOccurs': 'unbounded', 'type': 'AgilityVersion', 'name': 'versions', 'minOccurs': '0', 'native': False}})
        self.versions = versions 
