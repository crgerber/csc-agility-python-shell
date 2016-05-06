from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class VPCGatewayBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, vpngateway=None, properties=[], vpnconnection=None, vpc=None, customergateway=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'vpnGateway': {'type': 'VPNGateway', 'name': 'vpngateway', 'minOccurs': '0', 'native': False}, 'customerGateway': {'type': 'CustomerGateway', 'name': 'customergateway', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'vpc': {'type': 'VPC', 'name': 'vpc', 'minOccurs': '0', 'native': False}, 'vpnConnection': {'type': 'VPNConnection', 'name': 'vpnconnection', 'minOccurs': '0', 'native': False}})
        self.vpngateway = vpngateway
        self.properties = properties
        self.vpnconnection = vpnconnection
        self.vpc = vpc
        self.customergateway = customergateway 
