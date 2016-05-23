from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AuthenticationBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, orderposition=None, authgroups=[], properties=[], type=None, disabled=False):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'orderPosition': {'name': 'orderposition', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'authGroups': {'name': 'authgroups', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AuthGroup'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'type': {'name': 'type', 'native': False, 'type': 'Link'}, 'disabled': {'name': 'disabled', 'native': True, 'type': 'boolean'}})
        self.orderposition = orderposition
        self.authgroups = authgroups
        self.properties = properties
        self.type = type
        self.disabled = disabled 
