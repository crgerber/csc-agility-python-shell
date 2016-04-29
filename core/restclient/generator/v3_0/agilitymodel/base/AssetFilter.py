from .AgilityModelBase import AgilityModelBase

class AssetFilterBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, item=[], eval=[], match=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'item': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'item', 'minOccurs': '0', 'native': False}, 'match': {'maxOccurs': 'unbounded', 'type': 'AssetMatch', 'name': 'match', 'minOccurs': '0', 'native': False}, 'eval': {'maxOccurs': 'unbounded', 'type': 'Script', 'name': 'eval', 'minOccurs': '0', 'native': False}})
        self.item = item
        self.eval = eval
        self.match = match 
