from core.agility.v3_3.agilitymodel.base.Subnet import SubnetBase
from core.agility.v3_3.agilitymodel.actions.Subnet import SubnetActions

class Subnet(SubnetBase, SubnetActions):
    '''
    classdocs
    '''
    def __init__(self, tenantid=None, subnetid=None, network=None, availabilityzone=None, cidr=None, enabledhcp=None, ipversion=None, gatewayip=None, status=None):
        '''
        Constructor
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param network: network minOccurs=0
        @type network: Link
        @param availabilityzone: availabilityzone minOccurs=0
        @type availabilityzone: string
        @param cidr: cidr minOccurs=0
        @type cidr: string
        @param enabledhcp: enabledhcp minOccurs=0
        @type enabledhcp: boolean
        @param ipversion: ipversion minOccurs=0
        @type ipversion: int
        @param gatewayip: gatewayip minOccurs=0
        @type gatewayip: string
        @param status: status minOccurs=0
        @type status: string
        '''
        SubnetBase.__init__(self, tenantid=tenantid, subnetid=subnetid, network=network, availabilityzone=availabilityzone, cidr=cidr, enabledhcp=enabledhcp, ipversion=ipversion, gatewayip=gatewayip, status=status)
