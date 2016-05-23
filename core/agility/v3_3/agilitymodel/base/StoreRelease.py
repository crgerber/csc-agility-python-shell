from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StoreReleaseBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, product=None, editions=[], resources=[], build='', version=''):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'product': {'name': 'product', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'editions': {'name': 'editions', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'resources': {'name': 'resources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StoreResource'}, 'version': {'name': 'version', 'native': True, 'type': 'string'}, 'build': {'name': 'build', 'native': True, 'type': 'string'}})
        self.product = product
        self.editions = editions
        self.resources = resources
        self.build = build
        self.version = version 
