from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ProjectRoleBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, domain=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'domain': {'native': False, 'name': 'domain', 'minOccurs': '0', 'type': 'Link'}})
        self.domain = domain 
