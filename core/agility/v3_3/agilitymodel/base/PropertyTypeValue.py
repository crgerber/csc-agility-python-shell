from Asset import AssetBase

class PropertyTypeValueBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, child=[], displayname=None, parent=None, value=None, costvalue=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'costValue': {'type': 'CostValue', 'name': 'costvalue', 'minOccurs': '0', 'native': False}, 'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'value': {'type': 'string', 'name': 'value', 'minOccurs': '0', 'native': True}, 'parent': {'type': 'Link', 'name': 'parent', 'minOccurs': '0', 'native': False}, 'child': {'maxOccurs': 'unbounded', 'type': 'PropertyTypeValue', 'name': 'child', 'minOccurs': '0', 'native': False}})
        self.child = child
        self.displayname = displayname
        self.parent = parent
        self.value = value
        self.costvalue = costvalue 
