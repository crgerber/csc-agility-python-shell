from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class PolicyBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, type=None, apiversion=None, definition=None, scope=None, filter=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'filter': {'native': True, 'name': 'filter', 'minOccurs': '0', 'type': 'string'}, 'apiVersion': {'native': True, 'name': 'apiversion', 'minOccurs': '0', 'type': 'string'}, 'definition': {'native': True, 'name': 'definition', 'minOccurs': '0', 'type': 'string'}, 'scope': {'native': True, 'name': 'scope', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'PolicyType'}})
        self.type = type
        self.apiversion = apiversion
        self.definition = definition
        self.scope = scope
        self.filter = filter 
