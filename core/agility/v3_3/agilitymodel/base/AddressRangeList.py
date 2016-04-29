from core.agility.common.AgilityModelBase import AgilityModelBase

class AddressRangeListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, addressrange=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'AddressRange': {'maxOccurs': 'unbounded', 'native': False, 'name': 'addressrange', 'minOccurs': '0', 'type': 'AddressRange'}})
        self.addressrange = addressrange 
