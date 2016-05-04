from base.VPCSubnet import VPCSubnetBase
from actions.VPCSubnet import VPCSubnetActions

class VPCSubnet(VPCSubnetBase, VPCSubnetActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, vpcid=None, mappubliciponlaunch=None, cidrblock=None, interface=[], availabilityzone=None, defaultforavailibilityzone=None, subnetid=None, availableipaddresscount=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param mappubliciponlaunch: mappubliciponlaunch minOccurs=0
        @type mappubliciponlaunch: boolean
        @param cidrblock: cidrblock minOccurs=0
        @type cidrblock: string
        @param interface: interface minOccurs=0 maxOccurs=unbounded
        @type interface: Interface
        @param availabilityzone: availabilityzone minOccurs=0
        @type availabilityzone: string
        @param defaultforavailibilityzone: defaultforavailibilityzone minOccurs=0
        @type defaultforavailibilityzone: boolean
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param availableipaddresscount: availableipaddresscount minOccurs=0
        @type availableipaddresscount: int
        '''
        VPCSubnetBase.__init__(self, status=status, vpcid=vpcid, mappubliciponlaunch=mappubliciponlaunch, cidrblock=cidrblock, interface=interface, availabilityzone=availabilityzone, defaultforavailibilityzone=defaultforavailibilityzone, subnetid=subnetid, availableipaddresscount=availableipaddresscount)
