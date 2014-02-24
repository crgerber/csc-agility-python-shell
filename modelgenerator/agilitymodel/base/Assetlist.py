from AgilityModelBase import AgilityModelBase

class AssetlistBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, totalCount=None, offset=None, limit=None, Asset=list(), name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'totalCount': {'type': 'int', 'name': 'totalCount', 'native': True}, 'limit': {'type': 'int', 'name': 'limit', 'native': True}, 'Asset': {'maxOccurs': 'unbounded', 'type': 'Asset', 'name': 'Asset', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'offset': {'type': 'int', 'name': 'offset', 'native': True}})
        self.totalCount = totalCount
        self.offset = offset
        self.limit = limit
        self.Asset = Asset
        self.name = name 
