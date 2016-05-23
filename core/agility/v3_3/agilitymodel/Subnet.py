from core.agility.v3_3.agilitymodel.base.Subnet import SubnetBase
from core.agility.v3_3.agilitymodel.actions.Subnet import SubnetActions

class Subnet(SubnetBase, SubnetActions):
    '''
    classdocs
    '''
    def __init__(self, cidr=None, subnetid=None, enabledhcp=None, tenantid=None, gatewayip=None, availabilityzone=None, status=None, network=None, ipversion=None):
        '''
        Constructor
        @param cidr: cidr minOccurs=0
        @type cidr: string
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param enabledhcp: enabledhcp minOccurs=0
        @type enabledhcp: boolean
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param gatewayip: gatewayip minOccurs=0
        @type gatewayip: string
        @param availabilityzone: availabilityzone minOccurs=0
        @type availabilityzone: string
        @param status: status minOccurs=0
        @type status: string
        @param network: network minOccurs=0
        @type network: Link
        @param ipversion: ipversion minOccurs=0
        @type ipversion: int
        '''
        SubnetBase.__init__(self, cidr=cidr, subnetid=subnetid, enabledhcp=enabledhcp, tenantid=tenantid, gatewayip=gatewayip, availabilityzone=availabilityzone, status=status, network=network, ipversion=ipversion)
