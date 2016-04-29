from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class SdnItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, state=None, properties=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'state': {'native': False, 'name': 'state', 'minOccurs': '0', 'type': 'SdnState'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.state = state
        self.properties = properties 
