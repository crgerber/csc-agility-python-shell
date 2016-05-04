from core.agility.common.AgilityModelBase import AgilityModelBase

class SecurityGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, ingresspermission=[], vpcid=None, groupid=None, egresspermission=[], groupname=None, ownerid=None, groupdescription=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'ingressPermission': {'maxOccurs': 'unbounded', 'type': 'IpPermission', 'name': 'ingresspermission', 'minOccurs': '0', 'native': False}, 'vpcId': {'type': 'string', 'name': 'vpcid', 'minOccurs': '0', 'native': True}, 'groupDescription': {'type': 'string', 'name': 'groupdescription', 'minOccurs': '0', 'native': True}, 'egressPermission': {'maxOccurs': 'unbounded', 'type': 'IpPermission', 'name': 'egresspermission', 'minOccurs': '0', 'native': False}, 'groupName': {'type': 'string', 'name': 'groupname', 'minOccurs': '0', 'native': True}, 'ownerId': {'type': 'string', 'name': 'ownerid', 'minOccurs': '0', 'native': True}, 'groupId': {'type': 'string', 'name': 'groupid', 'minOccurs': '0', 'native': True}})
        self.ingresspermission = ingresspermission
        self.vpcid = vpcid
        self.groupid = groupid
        self.egresspermission = egresspermission
        self.groupname = groupname
        self.ownerid = ownerid
        self.groupdescription = groupdescription 
