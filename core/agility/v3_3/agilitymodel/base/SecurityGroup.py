from core.agility.common.AgilityModelBase import AgilityModelBase

class SecurityGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, groupdescription=None, groupid=None, vpcid=None, groupname=None, ownerid=None, egresspermission=[], ingresspermission=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'vpcId': {'native': True, 'name': 'vpcid', 'minOccurs': '0', 'type': 'string'}, 'groupId': {'native': True, 'name': 'groupid', 'minOccurs': '0', 'type': 'string'}, 'ownerId': {'native': True, 'name': 'ownerid', 'minOccurs': '0', 'type': 'string'}, 'groupDescription': {'native': True, 'name': 'groupdescription', 'minOccurs': '0', 'type': 'string'}, 'groupName': {'native': True, 'name': 'groupname', 'minOccurs': '0', 'type': 'string'}, 'egressPermission': {'maxOccurs': 'unbounded', 'native': False, 'name': 'egresspermission', 'minOccurs': '0', 'type': 'IpPermission'}, 'ingressPermission': {'maxOccurs': 'unbounded', 'native': False, 'name': 'ingresspermission', 'minOccurs': '0', 'type': 'IpPermission'}})
        self.groupdescription = groupdescription
        self.groupid = groupid
        self.vpcid = vpcid
        self.groupname = groupname
        self.ownerid = ownerid
        self.egresspermission = egresspermission
        self.ingresspermission = ingresspermission 
