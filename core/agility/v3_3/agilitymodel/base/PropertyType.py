from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, allowedassettype=None, open=False, rootvalue=[], owned=False, valueprovider=None, type=None, valueconstraint=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'allowedAssetType': {'type': 'Link', 'name': 'allowedassettype', 'minOccurs': '0', 'native': False}, 'type': {'type': 'PrimitiveType', 'name': 'type', 'minOccurs': '0', 'native': False}, 'rootValue': {'maxOccurs': 'unbounded', 'type': 'PropertyTypeValue', 'name': 'rootvalue', 'minOccurs': '0', 'native': False}, 'owned': {'type': 'boolean', 'name': 'owned', 'native': True}, 'valueProvider': {'type': 'string', 'name': 'valueprovider', 'minOccurs': '0', 'native': True}, 'open': {'type': 'boolean', 'name': 'open', 'native': True}, 'valueConstraint': {'type': 'ValueConstraintType', 'name': 'valueconstraint', 'minOccurs': '0', 'native': False}})
        self.displayname = displayname
        self.allowedassettype = allowedassettype
        self.open = open
        self.rootvalue = rootvalue
        self.owned = owned
        self.valueprovider = valueprovider
        self.type = type
        self.valueconstraint = valueconstraint 
