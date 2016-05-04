from Item import ItemBase

class AuthenticationBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, disabled=False, orderposition=None, type=None, properties=[], authgroups=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'disabled': {'type': 'boolean', 'name': 'disabled', 'native': True}, 'type': {'type': 'Link', 'name': 'type', 'native': False}, 'orderPosition': {'type': 'int', 'name': 'orderposition', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'authGroups': {'maxOccurs': 'unbounded', 'type': 'AuthGroup', 'name': 'authgroups', 'minOccurs': '0', 'native': False}})
        self.disabled = disabled
        self.orderposition = orderposition
        self.type = type
        self.properties = properties
        self.authgroups = authgroups 
