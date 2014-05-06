from core.agility.common.AgilityModelBase import AgilityModelBase


class AddressRangeListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, AddressRange=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'AddressRange': {'maxOccurs': 'unbounded', 'type': 'AddressRange', 'name': 'AddressRange', 'minOccurs': '0', 'native': False}})
        self.AddressRange = AddressRange 
