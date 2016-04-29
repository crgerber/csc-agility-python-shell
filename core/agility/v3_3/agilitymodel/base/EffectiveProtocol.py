from core.agility.v3_3.agilitymodel.base.Protocol import ProtocolBase

class EffectiveProtocolBase(ProtocolBase):
    '''
    classdocs
    '''
    def __init__(self, direction=None, status=None, policyname=None):
        ProtocolBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'direction': {'native': True, 'name': 'direction', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'policyName': {'native': True, 'name': 'policyname', 'minOccurs': '0', 'type': 'string'}})
        self.direction = direction
        self.status = status
        self.policyname = policyname 
