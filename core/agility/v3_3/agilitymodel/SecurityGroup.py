from core.agility.v3_3.agilitymodel.base.SecurityGroup import SecurityGroupBase
from core.agility.v3_3.agilitymodel.actions.SecurityGroup import SecurityGroupActions

class SecurityGroup(SecurityGroupBase, SecurityGroupActions):
    '''
    classdocs
    '''
    def __init__(self, ingresspermission=[], vpcid=None, groupid=None, egresspermission=[], groupname=None, ownerid=None, groupdescription=None):
        '''
        Constructor
        @param ingresspermission: ingresspermission minOccurs=0 maxOccurs=unbounded
        @type ingresspermission: IpPermission
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param groupid: groupid minOccurs=0
        @type groupid: string
        @param egresspermission: egresspermission minOccurs=0 maxOccurs=unbounded
        @type egresspermission: IpPermission
        @param groupname: groupname minOccurs=0
        @type groupname: string
        @param ownerid: ownerid minOccurs=0
        @type ownerid: string
        @param groupdescription: groupdescription minOccurs=0
        @type groupdescription: string
        '''
        SecurityGroupBase.__init__(self, ingresspermission=ingresspermission, vpcid=vpcid, groupid=groupid, egresspermission=egresspermission, groupname=groupname, ownerid=ownerid, groupdescription=groupdescription)
