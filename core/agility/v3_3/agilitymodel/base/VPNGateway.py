from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VPNGatewayBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, attachment=[], vpngatewayid=None, availabilityzone=None, status=None, type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'attachment': {'maxOccurs': 'unbounded', 'native': False, 'name': 'attachment', 'minOccurs': '0', 'type': 'AttachmentType'}, 'vpnGatewayId': {'native': True, 'name': 'vpngatewayid', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'availabilityZone': {'native': True, 'name': 'availabilityzone', 'minOccurs': '0', 'type': 'string'}})
        self.attachment = attachment
        self.vpngatewayid = vpngatewayid
        self.availabilityzone = availabilityzone
        self.status = status
        self.type = type 
