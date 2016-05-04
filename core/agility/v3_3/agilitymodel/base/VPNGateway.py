from Item import ItemBase

class VPNGatewayBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, availabilityzone=None, type=None, vpngatewayid=None, attachment=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'availabilityZone': {'type': 'string', 'name': 'availabilityzone', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'vpnGatewayId': {'type': 'string', 'name': 'vpngatewayid', 'minOccurs': '0', 'native': True}, 'attachment': {'maxOccurs': 'unbounded', 'type': 'AttachmentType', 'name': 'attachment', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.availabilityzone = availabilityzone
        self.type = type
        self.vpngatewayid = vpngatewayid
        self.attachment = attachment 
