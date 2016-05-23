from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class RouterBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, tenantid=None, status=None, adminstateup=None, routerid=None, externalnetwork=None, networkprovider=None, routerinterfaces=[]):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'tenantId': {'name': 'tenantid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'adminStateUp': {'name': 'adminstateup', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'routerId': {'name': 'routerid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'routerInterfaces': {'name': 'routerinterfaces', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'RouterInterface'}, 'externalNetwork': {'name': 'externalnetwork', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'networkProvider': {'name': 'networkprovider', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.tenantid = tenantid
        self.status = status
        self.adminstateup = adminstateup
        self.routerid = routerid
        self.externalnetwork = externalnetwork
        self.networkprovider = networkprovider
        self.routerinterfaces = routerinterfaces 
