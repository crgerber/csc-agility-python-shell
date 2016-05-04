from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class PortBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, macaddress=None, portid=None, network=None, adminstateup=None, deviceowner=None, tenantid=None, deviceid=None, fixedips=[]):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'macAddress': {'type': 'string', 'name': 'macaddress', 'minOccurs': '0', 'native': True}, 'portId': {'type': 'string', 'name': 'portid', 'minOccurs': '0', 'native': True}, 'network': {'type': 'Link', 'name': 'network', 'minOccurs': '0', 'native': False}, 'adminStateUp': {'type': 'boolean', 'name': 'adminstateup', 'minOccurs': '0', 'native': True}, 'deviceOwner': {'type': 'string', 'name': 'deviceowner', 'minOccurs': '0', 'native': True}, 'tenantId': {'type': 'string', 'name': 'tenantid', 'minOccurs': '0', 'native': True}, 'deviceId': {'type': 'string', 'name': 'deviceid', 'minOccurs': '0', 'native': True}, 'fixedIps': {'maxOccurs': 'unbounded', 'type': 'FixedIP', 'name': 'fixedips', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.macaddress = macaddress
        self.portid = portid
        self.network = network
        self.adminstateup = adminstateup
        self.deviceowner = deviceowner
        self.tenantid = tenantid
        self.deviceid = deviceid
        self.fixedips = fixedips 
