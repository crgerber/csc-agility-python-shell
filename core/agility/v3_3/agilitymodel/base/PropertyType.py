from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, valueprovider=None, displayname=None, valueconstraint=None, allowedassettype=None, rootvalue=[], owned=False, open=False, type=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'valueProvider': {'name': 'valueprovider', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'valueConstraint': {'name': 'valueconstraint', 'minOccurs': '0', 'native': False, 'type': 'ValueConstraintType'}, 'allowedAssetType': {'name': 'allowedassettype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'rootValue': {'name': 'rootvalue', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyTypeValue'}, 'owned': {'name': 'owned', 'native': True, 'type': 'boolean'}, 'open': {'name': 'open', 'native': True, 'type': 'boolean'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': False, 'type': 'PrimitiveType'}})
        self.valueprovider = valueprovider
        self.displayname = displayname
        self.valueconstraint = valueconstraint
        self.allowedassettype = allowedassettype
        self.rootvalue = rootvalue
        self.owned = owned
        self.open = open
        self.type = type 
