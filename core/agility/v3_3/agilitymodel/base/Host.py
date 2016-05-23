from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class HostBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, address=None, credential=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'address': {'name': 'address', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'credential': {'name': 'credential', 'minOccurs': '0', 'native': False, 'type': 'Credential'}})
        self.address = address
        self.credential = credential 
