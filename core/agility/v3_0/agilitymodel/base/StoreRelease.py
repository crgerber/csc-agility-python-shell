from core.agility.v3_0.agilitymodel.base.Item import ItemBase

class StoreReleaseBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, editions=[], product=None, version='', build='', resources=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'editions': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'editions', 'minOccurs': '0', 'native': False}, 'product': {'type': 'Link', 'name': 'product', 'minOccurs': '0', 'native': False}, 'version': {'type': 'string', 'name': 'version', 'native': True}, 'build': {'type': 'string', 'name': 'build', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resources', 'minOccurs': '0', 'native': False}})
        self.editions = editions
        self.product = product
        self.version = version
        self.build = build
        self.resources = resources 
