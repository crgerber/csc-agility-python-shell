from core.agility.common.AgilityModelBase import AgilityModelBase


class LdapGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, mapId=None, ldapGroupName='', agilityGroupName=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'ldapGroupName': {'type': 'string', 'name': 'ldapGroupName', 'native': True}, 'mapId': {'type': 'int', 'name': 'mapId', 'minOccurs': '0', 'native': True}, 'agilityGroupName': {'type': 'string', 'name': 'agilityGroupName', 'native': True}})
        self.mapId = mapId
        self.ldapGroupName = ldapGroupName
        self.agilityGroupName = agilityGroupName 
