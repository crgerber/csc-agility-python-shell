from .Item import ItemBase

class KerberosBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, hostname='', enabled=None, domainrealm=''):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'hostname': {'type': 'string', 'name': 'hostname', 'native': True}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'minOccurs': '0', 'native': True}, 'domainRealm': {'type': 'string', 'name': 'domainrealm', 'native': True}})
        self.hostname = hostname
        self.enabled = enabled
        self.domainrealm = domainrealm 
