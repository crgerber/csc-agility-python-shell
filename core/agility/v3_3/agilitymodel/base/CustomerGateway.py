from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class CustomerGatewayBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, ipaddress=None, customergatewayid=None, bgpasn=None, status=None, type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'ipAddress': {'native': True, 'name': 'ipaddress', 'minOccurs': '0', 'type': 'string'}, 'customerGatewayId': {'native': True, 'name': 'customergatewayid', 'minOccurs': '0', 'type': 'string'}, 'bgpAsn': {'native': True, 'name': 'bgpasn', 'minOccurs': '0', 'type': 'int'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}})
        self.ipaddress = ipaddress
        self.customergatewayid = customergatewayid
        self.bgpasn = bgpasn
        self.status = status
        self.type = type 
