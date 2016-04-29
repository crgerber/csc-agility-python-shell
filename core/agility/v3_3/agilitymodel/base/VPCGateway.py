from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class VPCGatewayBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, vpnconnection=None, vpc=None, customergateway=None, vpngateway=None, properties=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'vpnConnection': {'native': False, 'name': 'vpnconnection', 'minOccurs': '0', 'type': 'VPNConnection'}, 'vpc': {'native': False, 'name': 'vpc', 'minOccurs': '0', 'type': 'VPC'}, 'customerGateway': {'native': False, 'name': 'customergateway', 'minOccurs': '0', 'type': 'CustomerGateway'}, 'vpnGateway': {'native': False, 'name': 'vpngateway', 'minOccurs': '0', 'type': 'VPNGateway'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.vpnconnection = vpnconnection
        self.vpc = vpc
        self.customergateway = customergateway
        self.vpngateway = vpngateway
        self.properties = properties 
