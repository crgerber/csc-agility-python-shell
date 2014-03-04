from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class AddressListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, Address=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'Address': {'maxOccurs': 'unbounded', 'type': 'Address', 'name': 'Address', 'minOccurs': '0', 'native': False}})
        self.Address = Address 
