from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetFilterBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, eval=[], match=[], item=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'match': {'name': 'match', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetMatch'}, 'eval': {'name': 'eval', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Script'}, 'item': {'name': 'item', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.eval = eval
        self.match = match
        self.item = item 
