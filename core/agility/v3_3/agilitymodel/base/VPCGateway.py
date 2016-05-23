from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class VPCGatewayBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, customergateway=None, properties=[], vpnconnection=None, vpc=None, vpngateway=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customerGateway': {'name': 'customergateway', 'minOccurs': '0', 'native': False, 'type': 'CustomerGateway'}, 'vpnGateway': {'name': 'vpngateway', 'minOccurs': '0', 'native': False, 'type': 'VPNGateway'}, 'vpnConnection': {'name': 'vpnconnection', 'minOccurs': '0', 'native': False, 'type': 'VPNConnection'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'vpc': {'name': 'vpc', 'minOccurs': '0', 'native': False, 'type': 'VPC'}})
        self.customergateway = customergateway
        self.properties = properties
        self.vpnconnection = vpnconnection
        self.vpc = vpc
        self.vpngateway = vpngateway 
