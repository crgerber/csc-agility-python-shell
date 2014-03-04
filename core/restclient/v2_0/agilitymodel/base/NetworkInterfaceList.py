from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class NetworkInterfaceListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, NetworkInterface=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'NetworkInterface': {'maxOccurs': 'unbounded', 'type': 'NetworkInterface', 'name': 'NetworkInterface', 'minOccurs': '0', 'native': False}})
        self.NetworkInterface = NetworkInterface 
