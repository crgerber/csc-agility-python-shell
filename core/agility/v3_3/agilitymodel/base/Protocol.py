from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ProtocolBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, prefixes=[], maxport=None, protocol=None, minport=None, allowed=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'maxPort': {'native': True, 'name': 'maxport', 'minOccurs': '0', 'type': 'int'}, 'prefixes': {'maxOccurs': 'unbounded', 'native': True, 'name': 'prefixes', 'minOccurs': '0', 'type': 'string'}, 'allowed': {'native': True, 'name': 'allowed', 'minOccurs': '0', 'type': 'boolean'}, 'protocol': {'native': True, 'name': 'protocol', 'minOccurs': '0', 'type': 'string'}, 'minPort': {'native': True, 'name': 'minport', 'minOccurs': '0', 'type': 'int'}})
        self.prefixes = prefixes
        self.maxport = maxport
        self.protocol = protocol
        self.minport = minport
        self.allowed = allowed 
