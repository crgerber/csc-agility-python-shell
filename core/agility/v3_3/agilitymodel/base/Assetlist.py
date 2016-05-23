from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class AssetlistBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, name='', totalcount=None, limit=None, offset=None, asset=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'totalCount': {'name': 'totalcount', 'native': True, 'type': 'int'}, 'limit': {'name': 'limit', 'native': True, 'type': 'int'}, 'offset': {'name': 'offset', 'native': True, 'type': 'int'}, 'Asset': {'name': 'asset', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Asset'}})
        self.name = name
        self.totalcount = totalcount
        self.limit = limit
        self.offset = offset
        self.asset = asset 
