from core.agility.v3_3.agilitymodel.base.Interface import InterfaceBase
from core.agility.v3_3.agilitymodel.actions.Interface import InterfaceActions

class Interface(InterfaceBase, InterfaceActions):
    '''
    classdocs
    '''
    def __init__(self, networkinterfaceid=None, vpcid=None, subnetid=None, secondaryipaddress=[], primaryipaddress=None, description=None, location=None, macaddress=None, instanceid=None, status=None, instancestatus=None):
        '''
        Constructor
        @param networkinterfaceid: networkinterfaceid minOccurs=0
        @type networkinterfaceid: string
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param secondaryipaddress: secondaryipaddress minOccurs=0 maxOccurs=unbounded
        @type secondaryipaddress: string
        @param primaryipaddress: primaryipaddress minOccurs=0
        @type primaryipaddress: string
        @param description: description minOccurs=0
        @type description: string
        @param location: location minOccurs=0
        @type location: string
        @param macaddress: macaddress minOccurs=0
        @type macaddress: string
        @param instanceid: instanceid minOccurs=0
        @type instanceid: string
        @param status: status minOccurs=0
        @type status: string
        @param instancestatus: instancestatus minOccurs=0
        @type instancestatus: string
        '''
        InterfaceBase.__init__(self, networkinterfaceid=networkinterfaceid, vpcid=vpcid, subnetid=subnetid, secondaryipaddress=secondaryipaddress, primaryipaddress=primaryipaddress, description=description, location=location, macaddress=macaddress, instanceid=instanceid, status=status, instancestatus=instancestatus)
