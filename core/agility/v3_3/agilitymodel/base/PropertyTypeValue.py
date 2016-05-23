from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyTypeValueBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, value=None, displayname=None, child=[], parent=None, costvalue=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'costValue': {'name': 'costvalue', 'minOccurs': '0', 'native': False, 'type': 'CostValue'}, 'value': {'name': 'value', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'child': {'name': 'child', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyTypeValue'}, 'parent': {'name': 'parent', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.value = value
        self.displayname = displayname
        self.child = child
        self.parent = parent
        self.costvalue = costvalue 
