from core.agility.v3_3.agilitymodel.base.VPCSubnet import VPCSubnetBase
from core.agility.v3_3.agilitymodel.actions.VPCSubnet import VPCSubnetActions

class VPCSubnet(VPCSubnetBase, VPCSubnetActions):
    '''
    classdocs
    '''
    def __init__(self, vpcid=None, subnetid=None, interface=[], availabilityzone=None, defaultforavailibilityzone=None, cidrblock=None, mappubliciponlaunch=None, status=None, availableipaddresscount=None):
        '''
        Constructor
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param interface: interface minOccurs=0 maxOccurs=unbounded
        @type interface: Interface
        @param availabilityzone: availabilityzone minOccurs=0
        @type availabilityzone: string
        @param defaultforavailibilityzone: defaultforavailibilityzone minOccurs=0
        @type defaultforavailibilityzone: boolean
        @param cidrblock: cidrblock minOccurs=0
        @type cidrblock: string
        @param mappubliciponlaunch: mappubliciponlaunch minOccurs=0
        @type mappubliciponlaunch: boolean
        @param status: status minOccurs=0
        @type status: string
        @param availableipaddresscount: availableipaddresscount minOccurs=0
        @type availableipaddresscount: int
        '''
        VPCSubnetBase.__init__(self, vpcid=vpcid, subnetid=subnetid, interface=interface, availabilityzone=availabilityzone, defaultforavailibilityzone=defaultforavailibilityzone, cidrblock=cidrblock, mappubliciponlaunch=mappubliciponlaunch, status=status, availableipaddresscount=availableipaddresscount)
