from core.agility.common.AgilityModelBase import AgilityModelBase

class InternetGatewayBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, internetgatewayid=None, attachment=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'internetGatewayId': {'type': 'string', 'name': 'internetgatewayid', 'minOccurs': '0', 'native': True}, 'attachment': {'maxOccurs': 'unbounded', 'type': 'AttachmentType', 'name': 'attachment', 'minOccurs': '0', 'native': False}})
        self.internetgatewayid = internetgatewayid
        self.attachment = attachment 
