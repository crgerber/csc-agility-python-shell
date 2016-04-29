from core.agility.v3_3.agilitymodel.base.SecurityGroup import SecurityGroupBase
from core.agility.v3_3.agilitymodel.actions.SecurityGroup import SecurityGroupActions

class SecurityGroup(SecurityGroupBase, SecurityGroupActions):
    '''
    classdocs
    '''
    def __init__(self, groupdescription=None, groupid=None, vpcid=None, groupname=None, ownerid=None, egresspermission=[], ingresspermission=[]):
        '''
        Constructor
        @param groupdescription: groupdescription minOccurs=0
        @type groupdescription: string
        @param groupid: groupid minOccurs=0
        @type groupid: string
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param groupname: groupname minOccurs=0
        @type groupname: string
        @param ownerid: ownerid minOccurs=0
        @type ownerid: string
        @param egresspermission: egresspermission minOccurs=0 maxOccurs=unbounded
        @type egresspermission: IpPermission
        @param ingresspermission: ingresspermission minOccurs=0 maxOccurs=unbounded
        @type ingresspermission: IpPermission
        '''
        SecurityGroupBase.__init__(self, groupdescription=groupdescription, groupid=groupid, vpcid=vpcid, groupname=groupname, ownerid=ownerid, egresspermission=egresspermission, ingresspermission=ingresspermission)
