from core.agility.common.AgilityModelBase import AgilityModelBase

class LdapGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, mapid=None, agilitygroupname='', ldapgroupname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'mapId': {'name': 'mapid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'agilityGroupName': {'name': 'agilitygroupname', 'native': True, 'type': 'string'}, 'ldapGroupName': {'name': 'ldapgroupname', 'native': True, 'type': 'string'}})
        self.mapid = mapid
        self.agilitygroupname = agilitygroupname
        self.ldapgroupname = ldapgroupname 
