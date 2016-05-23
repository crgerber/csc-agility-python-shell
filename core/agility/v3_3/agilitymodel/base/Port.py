from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class PortBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, fixedips=[], network=None, status=None, deviceid=None, adminstateup=None, portid=None, deviceowner=None, macaddress=None, tenantid=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'portId': {'name': 'portid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'network': {'name': 'network', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'deviceId': {'name': 'deviceid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'adminStateUp': {'name': 'adminstateup', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'fixedIps': {'name': 'fixedips', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'FixedIP'}, 'deviceOwner': {'name': 'deviceowner', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'macAddress': {'name': 'macaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'tenantId': {'name': 'tenantid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.fixedips = fixedips
        self.network = network
        self.status = status
        self.deviceid = deviceid
        self.adminstateup = adminstateup
        self.portid = portid
        self.deviceowner = deviceowner
        self.macaddress = macaddress
        self.tenantid = tenantid 
