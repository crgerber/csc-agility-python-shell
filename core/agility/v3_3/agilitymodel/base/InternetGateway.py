from core.agility.common.AgilityModelBase import AgilityModelBase

class InternetGatewayBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, attachment=[], internetgatewayid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'attachment': {'name': 'attachment', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AttachmentType'}, 'internetGatewayId': {'name': 'internetgatewayid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.attachment = attachment
        self.internetgatewayid = internetgatewayid 
