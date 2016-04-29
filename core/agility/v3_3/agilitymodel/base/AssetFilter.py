from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetFilterBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, match=[], item=[], eval=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'match': {'maxOccurs': 'unbounded', 'native': False, 'name': 'match', 'minOccurs': '0', 'type': 'AssetMatch'}, 'item': {'maxOccurs': 'unbounded', 'native': False, 'name': 'item', 'minOccurs': '0', 'type': 'Link'}, 'eval': {'maxOccurs': 'unbounded', 'native': False, 'name': 'eval', 'minOccurs': '0', 'type': 'Script'}})
        self.match = match
        self.item = item
        self.eval = eval 
