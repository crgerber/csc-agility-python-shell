from core.agility.v3_3.agilitymodel.base.Interface import InterfaceBase
from core.agility.v3_3.agilitymodel.actions.Interface import InterfaceActions

class Interface(InterfaceBase, InterfaceActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, macaddress=None, vpcid=None, description=None, instancestatus=None, instanceid=None, networkinterfaceid=None, primaryipaddress=None, location=None, subnetid=None, secondaryipaddress=[]):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param macaddress: macaddress minOccurs=0
        @type macaddress: string
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param description: description minOccurs=0
        @type description: string
        @param instancestatus: instancestatus minOccurs=0
        @type instancestatus: string
        @param instanceid: instanceid minOccurs=0
        @type instanceid: string
        @param networkinterfaceid: networkinterfaceid minOccurs=0
        @type networkinterfaceid: string
        @param primaryipaddress: primaryipaddress minOccurs=0
        @type primaryipaddress: string
        @param location: location minOccurs=0
        @type location: string
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param secondaryipaddress: secondaryipaddress minOccurs=0 maxOccurs=unbounded
        @type secondaryipaddress: string
        '''
        InterfaceBase.__init__(self, status=status, macaddress=macaddress, vpcid=vpcid, description=description, instancestatus=instancestatus, instanceid=instanceid, networkinterfaceid=networkinterfaceid, primaryipaddress=primaryipaddress, location=location, subnetid=subnetid, secondaryipaddress=secondaryipaddress)
