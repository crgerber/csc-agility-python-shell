from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class CustomerGatewayBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, bgpasn=None, ipaddress=None, status=None, type=None, customergatewayid=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'customerGatewayId': {'name': 'customergatewayid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'bgpAsn': {'name': 'bgpasn', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'ipAddress': {'name': 'ipaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.bgpasn = bgpasn
        self.ipaddress = ipaddress
        self.status = status
        self.type = type
        self.customergatewayid = customergatewayid 
