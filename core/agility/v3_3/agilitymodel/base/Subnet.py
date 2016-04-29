from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class SubnetBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, tenantid=None, subnetid=None, network=None, availabilityzone=None, cidr=None, enabledhcp=None, ipversion=None, gatewayip=None, status=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'tenantId': {'native': True, 'name': 'tenantid', 'minOccurs': '0', 'type': 'string'}, 'ipVersion': {'native': True, 'name': 'ipversion', 'minOccurs': '0', 'type': 'int'}, 'gatewayIp': {'native': True, 'name': 'gatewayip', 'minOccurs': '0', 'type': 'string'}, 'availabilityZone': {'native': True, 'name': 'availabilityzone', 'minOccurs': '0', 'type': 'string'}, 'cidr': {'native': True, 'name': 'cidr', 'minOccurs': '0', 'type': 'string'}, 'enableDhcp': {'native': True, 'name': 'enabledhcp', 'minOccurs': '0', 'type': 'boolean'}, 'subnetId': {'native': True, 'name': 'subnetid', 'minOccurs': '0', 'type': 'string'}, 'network': {'native': False, 'name': 'network', 'minOccurs': '0', 'type': 'Link'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}})
        self.tenantid = tenantid
        self.subnetid = subnetid
        self.network = network
        self.availabilityzone = availabilityzone
        self.cidr = cidr
        self.enabledhcp = enabledhcp
        self.ipversion = ipversion
        self.gatewayip = gatewayip
        self.status = status 
