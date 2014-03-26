from AgilityModelBase import AgilityModelBase

class AssetlistBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, totalcount=None, offset=None, limit=None, asset=[], name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'totalCount': {'type': 'int', 'name': 'totalcount', 'native': True}, 'limit': {'type': 'int', 'name': 'limit', 'native': True}, 'Asset': {'maxOccurs': 'unbounded', 'type': 'Asset', 'name': 'asset', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'offset': {'type': 'int', 'name': 'offset', 'native': True}})
        self.totalcount = totalcount
        self.offset = offset
        self.limit = limit
        self.asset = asset
        self.name = name 
