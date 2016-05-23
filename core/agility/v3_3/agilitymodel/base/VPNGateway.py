from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VPNGatewayBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, attachment=[], vpngatewayid=None, status=None, type=None, availabilityzone=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'attachment': {'name': 'attachment', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AttachmentType'}, 'vpnGatewayId': {'name': 'vpngatewayid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'availabilityZone': {'name': 'availabilityzone', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.attachment = attachment
        self.vpngatewayid = vpngatewayid
        self.status = status
        self.type = type
        self.availabilityzone = availabilityzone 
