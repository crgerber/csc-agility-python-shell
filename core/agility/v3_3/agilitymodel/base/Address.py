from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AddressBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, instance=None, inetaddr=None, elastic=None, address=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'inetAddr': {'native': True, 'name': 'inetaddr', 'minOccurs': '0', 'type': 'string'}, 'elastic': {'native': True, 'name': 'elastic', 'minOccurs': '0', 'type': 'boolean'}, 'instance': {'native': False, 'name': 'instance', 'minOccurs': '0', 'type': 'Link'}, 'address': {'native': True, 'name': 'address', 'minOccurs': '0', 'type': 'string'}})
        self.instance = instance
        self.inetaddr = inetaddr
        self.elastic = elastic
        self.address = address 
