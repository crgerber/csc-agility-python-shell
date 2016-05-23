from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class SecurityRoleBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, product=None, enabled=None, visible=None, securityrolename=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'product': {'name': 'product', 'minOccurs': '0', 'native': False, 'type': 'Product'}, 'enabled': {'name': 'enabled', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'visible': {'name': 'visible', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'securityRoleName': {'name': 'securityrolename', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.product = product
        self.enabled = enabled
        self.visible = visible
        self.securityrolename = securityrolename 
