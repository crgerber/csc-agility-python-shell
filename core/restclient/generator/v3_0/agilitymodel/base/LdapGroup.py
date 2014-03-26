from AgilityModelBase import AgilityModelBase

class LdapGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, mapid=None, ldapgroupname='', agilitygroupname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'ldapGroupName': {'type': 'string', 'name': 'ldapgroupname', 'native': True}, 'mapId': {'type': 'int', 'name': 'mapid', 'minOccurs': '0', 'native': True}, 'agilityGroupName': {'type': 'string', 'name': 'agilitygroupname', 'native': True}})
        self.mapid = mapid
        self.ldapgroupname = ldapgroupname
        self.agilitygroupname = agilitygroupname 
