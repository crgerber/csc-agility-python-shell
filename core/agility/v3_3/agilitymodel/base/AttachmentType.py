from core.agility.common.AgilityModelBase import AgilityModelBase

class AttachmentTypeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, vpcid=None, state=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'vpcId': {'native': True, 'name': 'vpcid', 'minOccurs': '0', 'type': 'string'}, 'state': {'native': True, 'name': 'state', 'minOccurs': '0', 'type': 'string'}})
        self.vpcid = vpcid
        self.state = state 
