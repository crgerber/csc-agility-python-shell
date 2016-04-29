from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class HostBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, credential=None, address=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credential': {'native': False, 'name': 'credential', 'minOccurs': '0', 'type': 'Credential'}, 'address': {'native': True, 'name': 'address', 'minOccurs': '0', 'type': 'string'}})
        self.credential = credential
        self.address = address 
