from Protocol import ProtocolBase

class EffectiveProtocolBase(ProtocolBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, policyName=None, direction=None):
        ProtocolBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'policyName': {'type': 'string', 'name': 'policyName', 'minOccurs': '0', 'native': True}, 'direction': {'type': 'string', 'name': 'direction', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.policyName = policyName
        self.direction = direction 
