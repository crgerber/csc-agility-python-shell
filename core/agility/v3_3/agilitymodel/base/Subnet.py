from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class SubnetBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, cidr=None, subnetid=None, enabledhcp=None, tenantid=None, gatewayip=None, availabilityzone=None, status=None, network=None, ipversion=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cidr': {'name': 'cidr', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'subnetId': {'name': 'subnetid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'enableDhcp': {'name': 'enabledhcp', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'tenantId': {'name': 'tenantid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'gatewayIp': {'name': 'gatewayip', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'availabilityZone': {'name': 'availabilityzone', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'ipVersion': {'name': 'ipversion', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'network': {'name': 'network', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.cidr = cidr
        self.subnetid = subnetid
        self.enabledhcp = enabledhcp
        self.tenantid = tenantid
        self.gatewayip = gatewayip
        self.availabilityzone = availabilityzone
        self.status = status
        self.network = network
        self.ipversion = ipversion 
