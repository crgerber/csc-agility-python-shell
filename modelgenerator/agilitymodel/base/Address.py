from Item import ItemBase

class AddressBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, instance=None, inetAddr=None, address=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'instance': {'type': 'Link', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'address': {'type': 'string', 'name': 'address', 'minOccurs': '0', 'native': True}, 'inetAddr': {'type': 'string', 'name': 'inetAddr', 'minOccurs': '0', 'native': True}})
        self.instance = instance
        self.inetAddr = inetAddr
        self.address = address 
