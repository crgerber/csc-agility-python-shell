from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, valueprovider=None, rootvalue=[], open=False, valueconstraint=None, allowedassettype=None, owned=False, displayname=None, type=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'valueProvider': {'native': True, 'name': 'valueprovider', 'minOccurs': '0', 'type': 'string'}, 'rootValue': {'maxOccurs': 'unbounded', 'native': False, 'name': 'rootvalue', 'minOccurs': '0', 'type': 'PropertyTypeValue'}, 'open': {'native': True, 'name': 'open', 'type': 'boolean'}, 'valueConstraint': {'native': False, 'name': 'valueconstraint', 'minOccurs': '0', 'type': 'ValueConstraintType'}, 'allowedAssetType': {'native': False, 'name': 'allowedassettype', 'minOccurs': '0', 'type': 'Link'}, 'owned': {'native': True, 'name': 'owned', 'type': 'boolean'}, 'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'PrimitiveType'}})
        self.valueprovider = valueprovider
        self.rootvalue = rootvalue
        self.open = open
        self.valueconstraint = valueconstraint
        self.allowedassettype = allowedassettype
        self.owned = owned
        self.displayname = displayname
        self.type = type 
