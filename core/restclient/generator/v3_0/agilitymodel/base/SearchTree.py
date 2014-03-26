from AgilityModelBase import AgilityModelBase

class SearchTreeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, assetlist=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'Assetlist': {'maxOccurs': 'unbounded', 'type': 'Assetlist', 'name': 'assetlist', 'minOccurs': '0', 'native': False}})
        self.assetlist = assetlist 
