from core.agility.common.AgilityModelBase import AgilityModelBase

class AuthGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, authgroupname='', authserver=None, mapid=None, agilityusergroups=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'authGroupName': {'native': True, 'name': 'authgroupname', 'type': 'string'}, 'mapId': {'native': True, 'name': 'mapid', 'minOccurs': '0', 'type': 'int'}, 'authServer': {'native': False, 'name': 'authserver', 'minOccurs': '0', 'type': 'Link'}, 'agilityUserGroups': {'maxOccurs': 'unbounded', 'native': False, 'name': 'agilityusergroups', 'minOccurs': '0', 'type': 'Link'}})
        self.authgroupname = authgroupname
        self.authserver = authserver
        self.mapid = mapid
        self.agilityusergroups = agilityusergroups 
