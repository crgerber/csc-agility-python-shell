from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class PropertyTypeValueBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, parent=None, value=None, child=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}, 'value': {'type': 'string', 'name': 'value', 'minOccurs': '0', 'native': True}, 'parent': {'type': 'Link', 'name': 'parent', 'minOccurs': '0', 'native': False}, 'child': {'maxOccurs': 'unbounded', 'type': 'PropertyTypeValue', 'name': 'child', 'minOccurs': '0', 'native': False}})
        self.displayName = displayName
        self.parent = parent
        self.value = value
        self.child = child 
