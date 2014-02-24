from Asset import AssetBase

class ProtocolBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, prefixes=list(), protocol=None, minPort=None, maxPort=None, allowed=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'prefixes': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'prefixes', 'minOccurs': '0', 'native': True}, 'maxPort': {'type': 'int', 'name': 'maxPort', 'minOccurs': '0', 'native': True}, 'minPort': {'type': 'int', 'name': 'minPort', 'minOccurs': '0', 'native': True}, 'protocol': {'type': 'string', 'name': 'protocol', 'minOccurs': '0', 'native': True}, 'allowed': {'type': 'boolean', 'name': 'allowed', 'minOccurs': '0', 'native': True}})
        self.prefixes = prefixes
        self.protocol = protocol
        self.minPort = minPort
        self.maxPort = maxPort
        self.allowed = allowed 
