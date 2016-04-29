from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class RouterBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, tenantid=None, routerinterfaces=[], networkprovider=None, externalnetwork=None, adminstateup=None, routerid=None, status=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'routerId': {'native': True, 'name': 'routerid', 'minOccurs': '0', 'type': 'string'}, 'tenantId': {'native': True, 'name': 'tenantid', 'minOccurs': '0', 'type': 'string'}, 'externalNetwork': {'native': False, 'name': 'externalnetwork', 'minOccurs': '0', 'type': 'Link'}, 'adminStateUp': {'native': True, 'name': 'adminstateup', 'minOccurs': '0', 'type': 'boolean'}, 'networkProvider': {'native': False, 'name': 'networkprovider', 'minOccurs': '0', 'type': 'Link'}, 'routerInterfaces': {'maxOccurs': 'unbounded', 'native': False, 'name': 'routerinterfaces', 'minOccurs': '0', 'type': 'RouterInterface'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}})
        self.tenantid = tenantid
        self.routerinterfaces = routerinterfaces
        self.networkprovider = networkprovider
        self.externalnetwork = externalnetwork
        self.adminstateup = adminstateup
        self.routerid = routerid
        self.status = status 
