from SdnItem import SdnItemBase

class RouterBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, adminstateup=None, networkprovider=None, tenantid=None, routerid=None, externalnetwork=None, routerinterfaces=[]):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'adminStateUp': {'type': 'boolean', 'name': 'adminstateup', 'minOccurs': '0', 'native': True}, 'networkProvider': {'type': 'Link', 'name': 'networkprovider', 'minOccurs': '0', 'native': False}, 'tenantId': {'type': 'string', 'name': 'tenantid', 'minOccurs': '0', 'native': True}, 'routerId': {'type': 'string', 'name': 'routerid', 'minOccurs': '0', 'native': True}, 'externalNetwork': {'type': 'Link', 'name': 'externalnetwork', 'minOccurs': '0', 'native': False}, 'routerInterfaces': {'maxOccurs': 'unbounded', 'type': 'RouterInterface', 'name': 'routerinterfaces', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.adminstateup = adminstateup
        self.networkprovider = networkprovider
        self.tenantid = tenantid
        self.routerid = routerid
        self.externalnetwork = externalnetwork
        self.routerinterfaces = routerinterfaces 
