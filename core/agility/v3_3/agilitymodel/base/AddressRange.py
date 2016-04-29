from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AddressRangeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, network=None, rangemin=None, inetmin=None, rangetype=None, inetmax=None, availableaddresses=[], rangemax=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'network': {'native': False, 'name': 'network', 'minOccurs': '0', 'type': 'Link'}, 'inetMin': {'native': True, 'name': 'inetmin', 'minOccurs': '0', 'type': 'string'}, 'rangeType': {'native': True, 'name': 'rangetype', 'minOccurs': '0', 'type': 'string'}, 'inetMax': {'native': True, 'name': 'inetmax', 'minOccurs': '0', 'type': 'string'}, 'availableAddresses': {'maxOccurs': 'unbounded', 'native': False, 'name': 'availableaddresses', 'minOccurs': '0', 'type': 'Address'}, 'rangeMax': {'native': True, 'name': 'rangemax', 'minOccurs': '0', 'type': 'string'}, 'rangeMin': {'native': True, 'name': 'rangemin', 'minOccurs': '0', 'type': 'string'}})
        self.network = network
        self.rangemin = rangemin
        self.inetmin = inetmin
        self.rangetype = rangetype
        self.inetmax = inetmax
        self.availableaddresses = availableaddresses
        self.rangemax = rangemax 
