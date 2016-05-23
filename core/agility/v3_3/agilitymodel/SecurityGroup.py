from core.agility.v3_3.agilitymodel.base.SecurityGroup import SecurityGroupBase
from core.agility.v3_3.agilitymodel.actions.SecurityGroup import SecurityGroupActions

class SecurityGroup(SecurityGroupBase, SecurityGroupActions):
    '''
    classdocs
    '''
    def __init__(self, ingresspermission=[], ownerid=None, groupname=None, egresspermission=[], groupid=None, groupdescription=None, vpcid=None):
        '''
        Constructor
        @param ingresspermission: ingresspermission minOccurs=0 maxOccurs=unbounded
        @type ingresspermission: IpPermission
        @param ownerid: ownerid minOccurs=0
        @type ownerid: string
        @param groupname: groupname minOccurs=0
        @type groupname: string
        @param egresspermission: egresspermission minOccurs=0 maxOccurs=unbounded
        @type egresspermission: IpPermission
        @param groupid: groupid minOccurs=0
        @type groupid: string
        @param groupdescription: groupdescription minOccurs=0
        @type groupdescription: string
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        '''
        SecurityGroupBase.__init__(self, ingresspermission=ingresspermission, ownerid=ownerid, groupname=groupname, egresspermission=egresspermission, groupid=groupid, groupdescription=groupdescription, vpcid=vpcid)
