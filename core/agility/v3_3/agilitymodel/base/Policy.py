from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class PolicyBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, filter=None, scope=None, apiversion=None, type=None, definition=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'filter': {'name': 'filter', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'scope': {'name': 'scope', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'definition': {'name': 'definition', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': False, 'type': 'PolicyType'}, 'apiVersion': {'name': 'apiversion', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.filter = filter
        self.scope = scope
        self.apiversion = apiversion
        self.type = type
        self.definition = definition 
