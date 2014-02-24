from Asset import AssetBase

class ProjectRoleBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, domain=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'domain': {'type': 'Link', 'name': 'domain', 'minOccurs': '0', 'native': False}})
        self.domain = domain 
