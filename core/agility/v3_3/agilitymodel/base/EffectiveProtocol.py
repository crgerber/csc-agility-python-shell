from core.agility.v3_3.agilitymodel.base.Protocol import ProtocolBase

class EffectiveProtocolBase(ProtocolBase):
    '''
    classdocs
    '''
    def __init__(self, policyname=None, direction=None, status=None):
        ProtocolBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'policyName': {'name': 'policyname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'direction': {'name': 'direction', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.policyname = policyname
        self.direction = direction
        self.status = status 
