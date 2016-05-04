from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class SubnetBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, availabilityzone=None, network=None, gatewayip=None, tenantid=None, ipversion=None, enabledhcp=None, subnetid=None, cidr=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'availabilityZone': {'type': 'string', 'name': 'availabilityzone', 'minOccurs': '0', 'native': True}, 'network': {'type': 'Link', 'name': 'network', 'minOccurs': '0', 'native': False}, 'gatewayIp': {'type': 'string', 'name': 'gatewayip', 'minOccurs': '0', 'native': True}, 'tenantId': {'type': 'string', 'name': 'tenantid', 'minOccurs': '0', 'native': True}, 'ipVersion': {'type': 'int', 'name': 'ipversion', 'minOccurs': '0', 'native': True}, 'enableDhcp': {'type': 'boolean', 'name': 'enabledhcp', 'minOccurs': '0', 'native': True}, 'subnetId': {'type': 'string', 'name': 'subnetid', 'minOccurs': '0', 'native': True}, 'cidr': {'type': 'string', 'name': 'cidr', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.availabilityzone = availabilityzone
        self.network = network
        self.gatewayip = gatewayip
        self.tenantid = tenantid
        self.ipversion = ipversion
        self.enabledhcp = enabledhcp
        self.subnetid = subnetid
        self.cidr = cidr 
