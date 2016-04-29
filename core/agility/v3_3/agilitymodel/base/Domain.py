from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class DomainBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, roles=[], users=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'roles': {'maxOccurs': 'unbounded', 'native': False, 'name': 'roles', 'minOccurs': '0', 'type': 'Link'}, 'users': {'maxOccurs': 'unbounded', 'native': False, 'name': 'users', 'minOccurs': '0', 'type': 'Link'}})
        self.roles = roles
        self.users = users 
