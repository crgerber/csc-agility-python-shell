from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class FloatingIPBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, floatingipid=None, fixedipaddress=None, networkprovider=None, tenantid=None, floatingnetwork=None, floatingipaddress=None, port=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'floatingIPId': {'type': 'string', 'name': 'floatingipid', 'minOccurs': '0', 'native': True}, 'networkProvider': {'type': 'Link', 'name': 'networkprovider', 'minOccurs': '0', 'native': False}, 'tenantId': {'type': 'string', 'name': 'tenantid', 'minOccurs': '0', 'native': True}, 'port': {'type': 'Link', 'name': 'port', 'minOccurs': '0', 'native': False}, 'floatingNetwork': {'type': 'Link', 'name': 'floatingnetwork', 'minOccurs': '0', 'native': False}, 'floatingIPAddress': {'type': 'string', 'name': 'floatingipaddress', 'minOccurs': '0', 'native': True}, 'fixedIPAddress': {'type': 'string', 'name': 'fixedipaddress', 'minOccurs': '0', 'native': True}})
        self.floatingipid = floatingipid
        self.fixedipaddress = fixedipaddress
        self.networkprovider = networkprovider
        self.tenantid = tenantid
        self.floatingnetwork = floatingnetwork
        self.floatingipaddress = floatingipaddress
        self.port = port 
