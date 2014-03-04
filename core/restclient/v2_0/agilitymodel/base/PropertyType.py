from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class PropertyTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, open=False, rootValue=list(), owned=False, valueProvider=None, type=None, valueConstraint=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}, 'type': {'type': 'PrimitiveType', 'name': 'type', 'minOccurs': '0', 'native': False}, 'rootValue': {'maxOccurs': 'unbounded', 'type': 'PropertyTypeValue', 'name': 'rootValue', 'minOccurs': '0', 'native': False}, 'owned': {'type': 'boolean', 'name': 'owned', 'native': True}, 'valueProvider': {'type': 'Link', 'name': 'valueProvider', 'minOccurs': '0', 'native': False}, 'open': {'type': 'boolean', 'name': 'open', 'native': True}, 'valueConstraint': {'type': 'ValueConstraintType', 'name': 'valueConstraint', 'minOccurs': '0', 'native': False}})
        self.displayName = displayName
        self.open = open
        self.rootValue = rootValue
        self.owned = owned
        self.valueProvider = valueProvider
        self.type = type
        self.valueConstraint = valueConstraint 
