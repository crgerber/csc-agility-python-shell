from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class PortBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, tenantid=None, fixedips=[], adminstateup=None, macaddress=None, deviceid=None, portid=None, deviceowner=None, status=None, network=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'network': {'native': False, 'name': 'network', 'minOccurs': '0', 'type': 'Link'}, 'tenantId': {'native': True, 'name': 'tenantid', 'minOccurs': '0', 'type': 'string'}, 'fixedIps': {'maxOccurs': 'unbounded', 'native': False, 'name': 'fixedips', 'minOccurs': '0', 'type': 'FixedIP'}, 'adminStateUp': {'native': True, 'name': 'adminstateup', 'minOccurs': '0', 'type': 'boolean'}, 'macAddress': {'native': True, 'name': 'macaddress', 'minOccurs': '0', 'type': 'string'}, 'portId': {'native': True, 'name': 'portid', 'minOccurs': '0', 'type': 'string'}, 'deviceOwner': {'native': True, 'name': 'deviceowner', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'deviceId': {'native': True, 'name': 'deviceid', 'minOccurs': '0', 'type': 'string'}})
        self.tenantid = tenantid
        self.fixedips = fixedips
        self.adminstateup = adminstateup
        self.macaddress = macaddress
        self.deviceid = deviceid
        self.portid = portid
        self.deviceowner = deviceowner
        self.status = status
        self.network = network 
