from core.agility.common.AgilityModelBase import AgilityModelBase

class VPCSubnetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, subnetid=None, status=None, availabilityzone=None, cidrblock=None, mappubliciponlaunch=None, interface=[], defaultforavailibilityzone=None, vpcid=None, availableipaddresscount=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'subnetId': {'name': 'subnetid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'vpcId': {'name': 'vpcid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'availabilityZone': {'name': 'availabilityzone', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'cidrBlock': {'name': 'cidrblock', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'interface': {'name': 'interface', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Interface'}, 'mapPublicIpOnLaunch': {'name': 'mappubliciponlaunch', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'defaultForAvailibilityZone': {'name': 'defaultforavailibilityzone', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'availableIpAddressCount': {'name': 'availableipaddresscount', 'minOccurs': '0', 'native': True, 'type': 'int'}})
        self.subnetid = subnetid
        self.status = status
        self.availabilityzone = availabilityzone
        self.cidrblock = cidrblock
        self.mappubliciponlaunch = mappubliciponlaunch
        self.interface = interface
        self.defaultforavailibilityzone = defaultforavailibilityzone
        self.vpcid = vpcid
        self.availableipaddresscount = availableipaddresscount 
