from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class CustomerGatewayBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, customergatewayid=None, status=None, type=None, ipaddress=None, bgpasn=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customerGatewayId': {'type': 'string', 'name': 'customergatewayid', 'minOccurs': '0', 'native': True}, 'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'ipAddress': {'type': 'string', 'name': 'ipaddress', 'minOccurs': '0', 'native': True}, 'bgpAsn': {'type': 'int', 'name': 'bgpasn', 'minOccurs': '0', 'native': True}})
        self.customergatewayid = customergatewayid
        self.status = status
        self.type = type
        self.ipaddress = ipaddress
        self.bgpasn = bgpasn 
