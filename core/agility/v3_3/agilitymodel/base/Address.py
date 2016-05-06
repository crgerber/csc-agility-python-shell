from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AddressBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, instance=None, inetaddr=None, elastic=None, address=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'instance': {'type': 'Link', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'address': {'type': 'string', 'name': 'address', 'minOccurs': '0', 'native': True}, 'elastic': {'type': 'boolean', 'name': 'elastic', 'minOccurs': '0', 'native': True}, 'inetAddr': {'type': 'string', 'name': 'inetaddr', 'minOccurs': '0', 'native': True}})
        self.instance = instance
        self.inetaddr = inetaddr
        self.elastic = elastic
        self.address = address 
