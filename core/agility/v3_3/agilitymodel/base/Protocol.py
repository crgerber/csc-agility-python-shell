from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ProtocolBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, maxport=None, allowed=None, minport=None, prefixes=[], protocol=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'maxPort': {'name': 'maxport', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'allowed': {'name': 'allowed', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'minPort': {'name': 'minport', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'prefixes': {'name': 'prefixes', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'protocol': {'name': 'protocol', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.maxport = maxport
        self.allowed = allowed
        self.minport = minport
        self.prefixes = prefixes
        self.protocol = protocol 
