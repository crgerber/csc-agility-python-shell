from core.agility.v3_3.agilitymodel.base.Interface import InterfaceBase
from core.agility.v3_3.agilitymodel.actions.Interface import InterfaceActions

class Interface(InterfaceBase, InterfaceActions):
    '''
    classdocs
    '''
    def __init__(self, description=None, subnetid=None, primaryipaddress=None, location=None, instanceid=None, instancestatus=None, macaddress=None, secondaryipaddress=[], networkinterfaceid=None, vpcid=None, status=None):
        '''
        Constructor
        @param description: description minOccurs=0
        @type description: string
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param primaryipaddress: primaryipaddress minOccurs=0
        @type primaryipaddress: string
        @param location: location minOccurs=0
        @type location: string
        @param instanceid: instanceid minOccurs=0
        @type instanceid: string
        @param instancestatus: instancestatus minOccurs=0
        @type instancestatus: string
        @param macaddress: macaddress minOccurs=0
        @type macaddress: string
        @param secondaryipaddress: secondaryipaddress minOccurs=0 maxOccurs=unbounded
        @type secondaryipaddress: string
        @param networkinterfaceid: networkinterfaceid minOccurs=0
        @type networkinterfaceid: string
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param status: status minOccurs=0
        @type status: string
        '''
        InterfaceBase.__init__(self, description=description, subnetid=subnetid, primaryipaddress=primaryipaddress, location=location, instanceid=instanceid, instancestatus=instancestatus, macaddress=macaddress, secondaryipaddress=secondaryipaddress, networkinterfaceid=networkinterfaceid, vpcid=vpcid, status=status)
