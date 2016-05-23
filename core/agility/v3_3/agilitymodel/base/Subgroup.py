from core.agility.common.AgilityModelBase import AgilityModelBase

class SubgroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, groupid=None, userid=None, groupname=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'groupId': {'name': 'groupid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'userId': {'name': 'userid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'groupName': {'name': 'groupname', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.groupid = groupid
        self.userid = userid
        self.groupname = groupname 
