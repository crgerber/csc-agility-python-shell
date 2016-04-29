from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class AssetlistBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, limit=None, name='', asset=[], totalcount=None, offset=None):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'limit': {'native': True, 'name': 'limit', 'type': 'int'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'Asset': {'maxOccurs': 'unbounded', 'native': False, 'name': 'asset', 'minOccurs': '0', 'type': 'Asset'}, 'totalCount': {'native': True, 'name': 'totalcount', 'type': 'int'}, 'offset': {'native': True, 'name': 'offset', 'type': 'int'}})
        self.limit = limit
        self.name = name
        self.asset = asset
        self.totalcount = totalcount
        self.offset = offset 
