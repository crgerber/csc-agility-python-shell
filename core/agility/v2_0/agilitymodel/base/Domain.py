from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class DomainBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, users=list(), roles=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'users': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'users', 'minOccurs': '0', 'native': False}, 'roles': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'roles', 'minOccurs': '0', 'native': False}})
        self.users = users
        self.roles = roles 
