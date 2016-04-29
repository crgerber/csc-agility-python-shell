from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class FloatingIPBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, floatingipaddress=None, tenantid=None, networkprovider=None, port=None, floatingipid=None, fixedipaddress=None, floatingnetwork=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'floatingIPAddress': {'native': True, 'name': 'floatingipaddress', 'minOccurs': '0', 'type': 'string'}, 'tenantId': {'native': True, 'name': 'tenantid', 'minOccurs': '0', 'type': 'string'}, 'networkProvider': {'native': False, 'name': 'networkprovider', 'minOccurs': '0', 'type': 'Link'}, 'floatingNetwork': {'native': False, 'name': 'floatingnetwork', 'minOccurs': '0', 'type': 'Link'}, 'fixedIPAddress': {'native': True, 'name': 'fixedipaddress', 'minOccurs': '0', 'type': 'string'}, 'floatingIPId': {'native': True, 'name': 'floatingipid', 'minOccurs': '0', 'type': 'string'}, 'port': {'native': False, 'name': 'port', 'minOccurs': '0', 'type': 'Link'}})
        self.floatingipaddress = floatingipaddress
        self.tenantid = tenantid
        self.networkprovider = networkprovider
        self.port = port
        self.floatingipid = floatingipid
        self.fixedipaddress = fixedipaddress
        self.floatingnetwork = floatingnetwork 
