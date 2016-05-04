from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VPNConnectionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, vpnconnectionid=None, status=None, customergatewayconfiguration=None, customergateway=None, vpngateway=None, type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'vpnConnectionId': {'type': 'string', 'name': 'vpnconnectionid', 'minOccurs': '0', 'native': True}, 'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'customerGatewayConfiguration': {'type': 'string', 'name': 'customergatewayconfiguration', 'minOccurs': '0', 'native': True}, 'customerGateway': {'type': 'CustomerGateway', 'name': 'customergateway', 'minOccurs': '0', 'native': False}, 'vpnGateway': {'type': 'VPNGateway', 'name': 'vpngateway', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}})
        self.vpnconnectionid = vpnconnectionid
        self.status = status
        self.customergatewayconfiguration = customergatewayconfiguration
        self.customergateway = customergateway
        self.vpngateway = vpngateway
        self.type = type 
