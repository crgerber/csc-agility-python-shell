from core.agility.v3_3.agilitymodel.base.VPCSubnet import VPCSubnetBase
from core.agility.v3_3.agilitymodel.actions.VPCSubnet import VPCSubnetActions

class VPCSubnet(VPCSubnetBase, VPCSubnetActions):
    '''
    classdocs
    '''
    def __init__(self, subnetid=None, status=None, availabilityzone=None, cidrblock=None, mappubliciponlaunch=None, interface=[], defaultforavailibilityzone=None, vpcid=None, availableipaddresscount=None):
        '''
        Constructor
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param status: status minOccurs=0
        @type status: string
        @param availabilityzone: availabilityzone minOccurs=0
        @type availabilityzone: string
        @param cidrblock: cidrblock minOccurs=0
        @type cidrblock: string
        @param mappubliciponlaunch: mappubliciponlaunch minOccurs=0
        @type mappubliciponlaunch: boolean
        @param interface: interface minOccurs=0 maxOccurs=unbounded
        @type interface: Interface
        @param defaultforavailibilityzone: defaultforavailibilityzone minOccurs=0
        @type defaultforavailibilityzone: boolean
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param availableipaddresscount: availableipaddresscount minOccurs=0
        @type availableipaddresscount: int
        '''
        VPCSubnetBase.__init__(self, subnetid=subnetid, status=status, availabilityzone=availabilityzone, cidrblock=cidrblock, mappubliciponlaunch=mappubliciponlaunch, interface=interface, defaultforavailibilityzone=defaultforavailibilityzone, vpcid=vpcid, availableipaddresscount=availableipaddresscount)
