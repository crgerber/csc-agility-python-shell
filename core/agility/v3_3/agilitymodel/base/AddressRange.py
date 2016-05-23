from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AddressRangeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, network=None, inetmax=None, rangemax=None, rangemin=None, rangetype=None, availableaddresses=[], inetmin=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'network': {'name': 'network', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'inetMax': {'name': 'inetmax', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'rangeMax': {'name': 'rangemax', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'rangeMin': {'name': 'rangemin', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'rangeType': {'name': 'rangetype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'availableAddresses': {'name': 'availableaddresses', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Address'}, 'inetMin': {'name': 'inetmin', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.network = network
        self.inetmax = inetmax
        self.rangemax = rangemax
        self.rangemin = rangemin
        self.rangetype = rangetype
        self.availableaddresses = availableaddresses
        self.inetmin = inetmin 
