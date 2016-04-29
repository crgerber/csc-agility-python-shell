from core.agility.common.AgilityModelBase import AgilityModelBase

class LdapGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, agilitygroupname='', ldapgroupname='', mapid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'ldapGroupName': {'native': True, 'name': 'ldapgroupname', 'type': 'string'}, 'agilityGroupName': {'native': True, 'name': 'agilitygroupname', 'type': 'string'}, 'mapId': {'native': True, 'name': 'mapid', 'minOccurs': '0', 'type': 'int'}})
        self.agilitygroupname = agilitygroupname
        self.ldapgroupname = ldapgroupname
        self.mapid = mapid 
