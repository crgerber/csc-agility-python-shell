from core.agility.v3_3.agilitymodel.base.Protocol import ProtocolBase

class EffectiveProtocolBase(ProtocolBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, policyname=None, direction=None):
        ProtocolBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'policyName': {'type': 'string', 'name': 'policyname', 'minOccurs': '0', 'native': True}, 'direction': {'type': 'string', 'name': 'direction', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.policyname = policyname
        self.direction = direction 
