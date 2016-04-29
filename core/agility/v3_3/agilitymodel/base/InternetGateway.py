from core.agility.common.AgilityModelBase import AgilityModelBase

class InternetGatewayBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, attachment=[], internetgatewayid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'attachment': {'maxOccurs': 'unbounded', 'native': False, 'name': 'attachment', 'minOccurs': '0', 'type': 'AttachmentType'}, 'internetGatewayId': {'native': True, 'name': 'internetgatewayid', 'minOccurs': '0', 'type': 'string'}})
        self.attachment = attachment
        self.internetgatewayid = internetgatewayid 
