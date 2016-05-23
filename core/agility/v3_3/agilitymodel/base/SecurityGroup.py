from core.agility.common.AgilityModelBase import AgilityModelBase

class SecurityGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, ingresspermission=[], ownerid=None, groupname=None, egresspermission=[], groupid=None, groupdescription=None, vpcid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'ingressPermission': {'name': 'ingresspermission', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'IpPermission'}, 'groupDescription': {'name': 'groupdescription', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'groupName': {'name': 'groupname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'egressPermission': {'name': 'egresspermission', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'IpPermission'}, 'groupId': {'name': 'groupid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'ownerId': {'name': 'ownerid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'vpcId': {'name': 'vpcid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.ingresspermission = ingresspermission
        self.ownerid = ownerid
        self.groupname = groupname
        self.egresspermission = egresspermission
        self.groupid = groupid
        self.groupdescription = groupdescription
        self.vpcid = vpcid 
