from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VPNConnectionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, vpnconnectionid=None, customergatewayconfiguration=None, customergateway=None, vpngateway=None, type=None, status=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'vpnConnectionId': {'name': 'vpnconnectionid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'customerGatewayConfiguration': {'name': 'customergatewayconfiguration', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'customerGateway': {'name': 'customergateway', 'minOccurs': '0', 'native': False, 'type': 'CustomerGateway'}, 'vpnGateway': {'name': 'vpngateway', 'minOccurs': '0', 'native': False, 'type': 'VPNGateway'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.vpnconnectionid = vpnconnectionid
        self.customergatewayconfiguration = customergatewayconfiguration
        self.customergateway = customergateway
        self.vpngateway = vpngateway
        self.type = type
        self.status = status 
