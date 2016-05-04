from core.agility.common.AgilityModelBase import AgilityModelBase

class AddressListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, address=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'Address': {'maxOccurs': 'unbounded', 'type': 'Address', 'name': 'address', 'minOccurs': '0', 'native': False}})
        self.address = address 
