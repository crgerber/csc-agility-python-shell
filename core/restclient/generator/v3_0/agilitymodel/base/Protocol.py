from .Asset import AssetBase

class ProtocolBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, prefixes=[], protocol=None, minport=None, maxport=None, allowed=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'prefixes': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'prefixes', 'minOccurs': '0', 'native': True}, 'maxPort': {'type': 'int', 'name': 'maxport', 'minOccurs': '0', 'native': True}, 'minPort': {'type': 'int', 'name': 'minport', 'minOccurs': '0', 'native': True}, 'protocol': {'type': 'string', 'name': 'protocol', 'minOccurs': '0', 'native': True}, 'allowed': {'type': 'boolean', 'name': 'allowed', 'minOccurs': '0', 'native': True}})
        self.prefixes = prefixes
        self.protocol = protocol
        self.minport = minport
        self.maxport = maxport
        self.allowed = allowed 
