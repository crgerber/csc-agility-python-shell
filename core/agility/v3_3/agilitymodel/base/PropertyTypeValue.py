from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyTypeValueBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, costvalue=None, parent=None, value=None, displayname=None, child=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'parent': {'native': False, 'name': 'parent', 'minOccurs': '0', 'type': 'Link'}, 'value': {'native': True, 'name': 'value', 'minOccurs': '0', 'type': 'string'}, 'costValue': {'native': False, 'name': 'costvalue', 'minOccurs': '0', 'type': 'CostValue'}, 'child': {'maxOccurs': 'unbounded', 'native': False, 'name': 'child', 'minOccurs': '0', 'type': 'PropertyTypeValue'}})
        self.costvalue = costvalue
        self.parent = parent
        self.value = value
        self.displayname = displayname
        self.child = child 
