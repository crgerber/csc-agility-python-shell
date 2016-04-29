from core.agility.common.AgilityModelBase import AgilityModelBase

class SubgroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, groupname=None, userid=None, groupid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'groupName': {'native': True, 'name': 'groupname', 'minOccurs': '0', 'type': 'string'}, 'userId': {'native': True, 'name': 'userid', 'minOccurs': '0', 'type': 'string'}, 'groupId': {'native': True, 'name': 'groupid', 'minOccurs': '0', 'type': 'string'}})
        self.groupname = groupname
        self.userid = userid
        self.groupid = groupid 
