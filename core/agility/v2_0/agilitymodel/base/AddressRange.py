from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class AddressRangeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, network=None, rangeType=None, inetMax=None, inetMin=None, availableAddresses=list(), rangeMax=None, rangeMin=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'network': {'type': 'Link', 'name': 'network', 'minOccurs': '0', 'native': False}, 'rangeType': {'type': 'string', 'name': 'rangeType', 'minOccurs': '0', 'native': True}, 'inetMax': {'type': 'string', 'name': 'inetMax', 'minOccurs': '0', 'native': True}, 'inetMin': {'type': 'string', 'name': 'inetMin', 'minOccurs': '0', 'native': True}, 'availableAddresses': {'maxOccurs': 'unbounded', 'type': 'Address', 'name': 'availableAddresses', 'minOccurs': '0', 'native': False}, 'rangeMax': {'type': 'string', 'name': 'rangeMax', 'minOccurs': '0', 'native': True}, 'rangeMin': {'type': 'string', 'name': 'rangeMin', 'minOccurs': '0', 'native': True}})
        self.network = network
        self.rangeType = rangeType
        self.inetMax = inetMax
        self.inetMin = inetMin
        self.availableAddresses = availableAddresses
        self.rangeMax = rangeMax
        self.rangeMin = rangeMin 
