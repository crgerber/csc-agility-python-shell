from VersionedItem import VersionedItemBase

class PolicyBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, filter=None, scope=None, type=None, apiversion=None, definition=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'filter': {'type': 'string', 'name': 'filter', 'minOccurs': '0', 'native': True}, 'scope': {'type': 'string', 'name': 'scope', 'minOccurs': '0', 'native': True}, 'type': {'type': 'PolicyType', 'name': 'type', 'minOccurs': '0', 'native': False}, 'apiVersion': {'type': 'string', 'name': 'apiversion', 'minOccurs': '0', 'native': True}, 'definition': {'type': 'string', 'name': 'definition', 'minOccurs': '0', 'native': True}})
        self.filter = filter
        self.scope = scope
        self.type = type
        self.apiversion = apiversion
        self.definition = definition 
