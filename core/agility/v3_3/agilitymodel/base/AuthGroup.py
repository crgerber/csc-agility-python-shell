from core.agility.common.AgilityModelBase import AgilityModelBase

class AuthGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, mapid=None, agilityusergroups=[], authserver=None, authgroupname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'authGroupName': {'name': 'authgroupname', 'native': True, 'type': 'string'}, 'mapId': {'name': 'mapid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'authServer': {'name': 'authserver', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'agilityUserGroups': {'name': 'agilityusergroups', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.mapid = mapid
        self.agilityusergroups = agilityusergroups
        self.authserver = authserver
        self.authgroupname = authgroupname 
