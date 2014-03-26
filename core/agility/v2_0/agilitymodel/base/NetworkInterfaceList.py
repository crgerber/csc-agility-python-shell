from core.agility.common.AgilityModelBase import AgilityModelBase


class NetworkInterfaceListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, NetworkInterface=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'NetworkInterface': {'maxOccurs': 'unbounded', 'type': 'NetworkInterface', 'name': 'NetworkInterface', 'minOccurs': '0', 'native': False}})
        self.NetworkInterface = NetworkInterface 
