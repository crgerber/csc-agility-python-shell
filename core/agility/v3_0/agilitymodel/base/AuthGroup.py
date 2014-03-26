from core.agility.common.AgilityModelBase import AgilityModelBase


class AuthGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, authserver=None, authgroupname='', mapid=None, agilityusergroups=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'authServer': {'type': 'Link', 'name': 'authserver', 'minOccurs': '0', 'native': False}, 'authGroupName': {'type': 'string', 'name': 'authgroupname', 'native': True}, 'mapId': {'type': 'int', 'name': 'mapid', 'minOccurs': '0', 'native': True}, 'agilityUserGroups': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'agilityusergroups', 'minOccurs': '0', 'native': False}})
        self.authserver = authserver
        self.authgroupname = authgroupname
        self.mapid = mapid
        self.agilityusergroups = agilityusergroups 
