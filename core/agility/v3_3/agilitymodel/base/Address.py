from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AddressBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, address=None, elastic=None, inetaddr=None, instance=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'address': {'name': 'address', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'elastic': {'name': 'elastic', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'inetAddr': {'name': 'inetaddr', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'instance': {'name': 'instance', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.address = address
        self.elastic = elastic
        self.inetaddr = inetaddr
        self.instance = instance 
