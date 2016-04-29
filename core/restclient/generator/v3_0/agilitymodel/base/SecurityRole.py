from .Item import ItemBase

class SecurityRoleBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, visible=None, product=None, enabled=None, securityrolename=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'visible': {'type': 'boolean', 'name': 'visible', 'minOccurs': '0', 'native': True}, 'product': {'type': 'Product', 'name': 'product', 'minOccurs': '0', 'native': False}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'minOccurs': '0', 'native': True}, 'securityRoleName': {'type': 'string', 'name': 'securityrolename', 'minOccurs': '0', 'native': True}})
        self.visible = visible
        self.product = product
        self.enabled = enabled
        self.securityrolename = securityrolename 
