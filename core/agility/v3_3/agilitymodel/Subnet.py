from core.agility.v3_3.agilitymodel.base.Subnet import SubnetBase
from core.agility.v3_3.agilitymodel.actions.Subnet import SubnetActions

class Subnet(SubnetBase, SubnetActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, availabilityzone=None, network=None, gatewayip=None, tenantid=None, ipversion=None, enabledhcp=None, subnetid=None, cidr=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param availabilityzone: availabilityzone minOccurs=0
        @type availabilityzone: string
        @param network: network minOccurs=0
        @type network: Link
        @param gatewayip: gatewayip minOccurs=0
        @type gatewayip: string
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param ipversion: ipversion minOccurs=0
        @type ipversion: int
        @param enabledhcp: enabledhcp minOccurs=0
        @type enabledhcp: boolean
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param cidr: cidr minOccurs=0
        @type cidr: string
        '''
        SubnetBase.__init__(self, status=status, availabilityzone=availabilityzone, network=network, gatewayip=gatewayip, tenantid=tenantid, ipversion=ipversion, enabledhcp=enabledhcp, subnetid=subnetid, cidr=cidr)
