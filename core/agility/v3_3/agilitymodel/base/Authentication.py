from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AuthenticationBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, orderposition=None, properties=[], disabled=False, authgroups=[], type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'orderPosition': {'native': True, 'name': 'orderposition', 'minOccurs': '0', 'type': 'int'}, 'type': {'native': False, 'name': 'type', 'type': 'Link'}, 'disabled': {'native': True, 'name': 'disabled', 'type': 'boolean'}, 'authGroups': {'maxOccurs': 'unbounded', 'native': False, 'name': 'authgroups', 'minOccurs': '0', 'type': 'AuthGroup'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.orderposition = orderposition
        self.properties = properties
        self.disabled = disabled
        self.authgroups = authgroups
        self.type = type 
