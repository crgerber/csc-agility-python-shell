from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class SecurityRoleBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, enabled=None, securityrolename=None, product=None, visible=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'enabled': {'native': True, 'name': 'enabled', 'minOccurs': '0', 'type': 'boolean'}, 'securityRoleName': {'native': True, 'name': 'securityrolename', 'minOccurs': '0', 'type': 'string'}, 'product': {'native': False, 'name': 'product', 'minOccurs': '0', 'type': 'Product'}, 'visible': {'native': True, 'name': 'visible', 'minOccurs': '0', 'type': 'boolean'}})
        self.enabled = enabled
        self.securityrolename = securityrolename
        self.product = product
        self.visible = visible 
