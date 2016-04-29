from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StoreReleaseBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, build='', resources=[], version='', editions=[], product=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'build': {'native': True, 'name': 'build', 'type': 'string'}, 'resources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resources', 'minOccurs': '0', 'type': 'StoreResource'}, 'version': {'native': True, 'name': 'version', 'type': 'string'}, 'editions': {'maxOccurs': 'unbounded', 'native': False, 'name': 'editions', 'minOccurs': '0', 'type': 'Link'}, 'product': {'native': False, 'name': 'product', 'minOccurs': '0', 'type': 'Link'}})
        self.build = build
        self.resources = resources
        self.version = version
        self.editions = editions
        self.product = product 
