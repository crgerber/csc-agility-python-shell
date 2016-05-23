from core.agility.common.AgilityModelBase import AgilityModelBase

class AttachmentTypeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, state=None, vpcid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'state': {'name': 'state', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'vpcId': {'name': 'vpcid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.state = state
        self.vpcid = vpcid 
