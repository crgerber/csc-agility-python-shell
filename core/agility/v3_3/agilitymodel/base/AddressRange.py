from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AddressRangeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, network=None, rangetype=None, inetmax=None, inetmin=None, availableaddresses=[], rangemax=None, rangemin=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'network': {'type': 'Link', 'name': 'network', 'minOccurs': '0', 'native': False}, 'rangeType': {'type': 'string', 'name': 'rangetype', 'minOccurs': '0', 'native': True}, 'inetMax': {'type': 'string', 'name': 'inetmax', 'minOccurs': '0', 'native': True}, 'inetMin': {'type': 'string', 'name': 'inetmin', 'minOccurs': '0', 'native': True}, 'availableAddresses': {'maxOccurs': 'unbounded', 'type': 'Address', 'name': 'availableaddresses', 'minOccurs': '0', 'native': False}, 'rangeMax': {'type': 'string', 'name': 'rangemax', 'minOccurs': '0', 'native': True}, 'rangeMin': {'type': 'string', 'name': 'rangemin', 'minOccurs': '0', 'native': True}})
        self.network = network
        self.rangetype = rangetype
        self.inetmax = inetmax
        self.inetmin = inetmin
        self.availableaddresses = availableaddresses
        self.rangemax = rangemax
        self.rangemin = rangemin 
