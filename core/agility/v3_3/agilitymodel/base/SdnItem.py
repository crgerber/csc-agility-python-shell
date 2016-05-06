from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class SdnItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, state=None, properties=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'state': {'type': 'SdnState', 'name': 'state', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.state = state
        self.properties = properties 
