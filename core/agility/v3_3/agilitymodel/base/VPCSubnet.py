from core.agility.common.AgilityModelBase import AgilityModelBase

class VPCSubnetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, vpcid=None, mappubliciponlaunch=None, cidrblock=None, interface=[], availabilityzone=None, defaultforavailibilityzone=None, subnetid=None, availableipaddresscount=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'mapPublicIpOnLaunch': {'type': 'boolean', 'name': 'mappubliciponlaunch', 'minOccurs': '0', 'native': True}, 'defaultForAvailibilityZone': {'type': 'boolean', 'name': 'defaultforavailibilityzone', 'minOccurs': '0', 'native': True}, 'availableIpAddressCount': {'type': 'int', 'name': 'availableipaddresscount', 'minOccurs': '0', 'native': True}, 'subnetId': {'type': 'string', 'name': 'subnetid', 'minOccurs': '0', 'native': True}, 'vpcId': {'type': 'string', 'name': 'vpcid', 'minOccurs': '0', 'native': True}, 'interface': {'maxOccurs': 'unbounded', 'type': 'Interface', 'name': 'interface', 'minOccurs': '0', 'native': False}, 'cidrBlock': {'type': 'string', 'name': 'cidrblock', 'minOccurs': '0', 'native': True}, 'availabilityZone': {'type': 'string', 'name': 'availabilityzone', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.vpcid = vpcid
        self.mappubliciponlaunch = mappubliciponlaunch
        self.cidrblock = cidrblock
        self.interface = interface
        self.availabilityzone = availabilityzone
        self.defaultforavailibilityzone = defaultforavailibilityzone
        self.subnetid = subnetid
        self.availableipaddresscount = availableipaddresscount 
