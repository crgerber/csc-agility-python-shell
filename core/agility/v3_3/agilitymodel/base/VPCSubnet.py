from core.agility.common.AgilityModelBase import AgilityModelBase

class VPCSubnetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, vpcid=None, subnetid=None, interface=[], availabilityzone=None, defaultforavailibilityzone=None, cidrblock=None, mappubliciponlaunch=None, status=None, availableipaddresscount=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'vpcId': {'native': True, 'name': 'vpcid', 'minOccurs': '0', 'type': 'string'}, 'subnetId': {'native': True, 'name': 'subnetid', 'minOccurs': '0', 'type': 'string'}, 'availabilityZone': {'native': True, 'name': 'availabilityzone', 'minOccurs': '0', 'type': 'string'}, 'defaultForAvailibilityZone': {'native': True, 'name': 'defaultforavailibilityzone', 'minOccurs': '0', 'type': 'boolean'}, 'cidrBlock': {'native': True, 'name': 'cidrblock', 'minOccurs': '0', 'type': 'string'}, 'mapPublicIpOnLaunch': {'native': True, 'name': 'mappubliciponlaunch', 'minOccurs': '0', 'type': 'boolean'}, 'interface': {'maxOccurs': 'unbounded', 'native': False, 'name': 'interface', 'minOccurs': '0', 'type': 'Interface'}, 'availableIpAddressCount': {'native': True, 'name': 'availableipaddresscount', 'minOccurs': '0', 'type': 'int'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}})
        self.vpcid = vpcid
        self.subnetid = subnetid
        self.interface = interface
        self.availabilityzone = availabilityzone
        self.defaultforavailibilityzone = defaultforavailibilityzone
        self.cidrblock = cidrblock
        self.mappubliciponlaunch = mappubliciponlaunch
        self.status = status
        self.availableipaddresscount = availableipaddresscount 
