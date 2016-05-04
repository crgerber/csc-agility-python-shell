from core.agility.common.AgilityModelBase import AgilityModelBase

class SubgroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, groupname=None, userid=None, groupid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'groupName': {'type': 'string', 'name': 'groupname', 'minOccurs': '0', 'native': True}, 'userId': {'type': 'string', 'name': 'userid', 'minOccurs': '0', 'native': True}, 'groupId': {'type': 'string', 'name': 'groupid', 'minOccurs': '0', 'native': True}})
        self.groupname = groupname
        self.userid = userid
        self.groupid = groupid 
