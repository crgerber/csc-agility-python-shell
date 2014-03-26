from Asset import AssetBase

class HostBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, credential=None, address=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credential': {'type': 'Credential', 'name': 'credential', 'minOccurs': '0', 'native': False}, 'address': {'type': 'string', 'name': 'address', 'minOccurs': '0', 'native': True}})
        self.credential = credential
        self.address = address 
