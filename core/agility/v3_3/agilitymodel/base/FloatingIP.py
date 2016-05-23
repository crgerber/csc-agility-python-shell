from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class FloatingIPBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, floatingipaddress=None, floatingnetwork=None, tenantid=None, port=None, floatingipid=None, fixedipaddress=None, networkprovider=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'floatingIPAddress': {'name': 'floatingipaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'floatingNetwork': {'name': 'floatingnetwork', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'tenantId': {'name': 'tenantid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'port': {'name': 'port', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'floatingIPId': {'name': 'floatingipid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'fixedIPAddress': {'name': 'fixedipaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'networkProvider': {'name': 'networkprovider', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.floatingipaddress = floatingipaddress
        self.floatingnetwork = floatingnetwork
        self.tenantid = tenantid
        self.port = port
        self.floatingipid = floatingipid
        self.fixedipaddress = fixedipaddress
        self.networkprovider = networkprovider 
