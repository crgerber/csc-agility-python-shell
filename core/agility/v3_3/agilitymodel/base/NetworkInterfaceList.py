from core.agility.common.AgilityModelBase import AgilityModelBase

class NetworkInterfaceListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, networkinterface=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'NetworkInterface': {'name': 'networkinterface', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'NetworkInterface'}})
        self.networkinterface = networkinterface 
