from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class DomainBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, roles=[], users=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'roles': {'name': 'roles', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'users': {'name': 'users', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.roles = roles
        self.users = users 
