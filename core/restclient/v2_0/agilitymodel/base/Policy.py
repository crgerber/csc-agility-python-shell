from core.restclient.v2_0.agilitymodel.base.VersionedItem import VersionedItemBase

class PolicyBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, filter=None, definition=None, type=None, apiVersion=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'filter': {'type': 'string', 'name': 'filter', 'minOccurs': '0', 'native': True}, 'definition': {'type': 'string', 'name': 'definition', 'minOccurs': '0', 'native': True}, 'type': {'type': 'PolicyType', 'name': 'type', 'minOccurs': '0', 'native': False}, 'apiVersion': {'type': 'string', 'name': 'apiVersion', 'minOccurs': '0', 'native': True}})
        self.filter = filter
        self.definition = definition
        self.type = type
        self.apiVersion = apiVersion 
