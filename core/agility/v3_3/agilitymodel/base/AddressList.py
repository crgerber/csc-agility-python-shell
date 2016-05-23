from core.agility.common.AgilityModelBase import AgilityModelBase

class AddressListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, address=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'Address': {'name': 'address', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Address'}})
        self.address = address 
