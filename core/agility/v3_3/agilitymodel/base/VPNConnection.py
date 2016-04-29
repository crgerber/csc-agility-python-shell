from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VPNConnectionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, customergateway=None, customergatewayconfiguration=None, vpnconnectionid=None, status=None, vpngateway=None, type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customerGateway': {'native': False, 'name': 'customergateway', 'minOccurs': '0', 'type': 'CustomerGateway'}, 'customerGatewayConfiguration': {'native': True, 'name': 'customergatewayconfiguration', 'minOccurs': '0', 'type': 'string'}, 'vpnConnectionId': {'native': True, 'name': 'vpnconnectionid', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'vpnGateway': {'native': False, 'name': 'vpngateway', 'minOccurs': '0', 'type': 'VPNGateway'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}})
        self.customergateway = customergateway
        self.customergatewayconfiguration = customergatewayconfiguration
        self.vpnconnectionid = vpnconnectionid
        self.status = status
        self.vpngateway = vpngateway
        self.type = type 
