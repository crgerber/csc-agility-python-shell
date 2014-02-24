from AgilityModelBase import AgilityModelBase

class EnvelopeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, pendingAsset=list(), Asset=list(), version='', productVersion=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'pendingAsset': {'maxOccurs': 'unbounded', 'type': 'Asset', 'name': 'pendingAsset', 'minOccurs': '0', 'native': False}, 'Asset': {'maxOccurs': 'unbounded', 'type': 'Asset', 'name': 'Asset', 'minOccurs': '0', 'native': False}, 'version': {'type': 'string', 'name': 'version', 'native': True}, 'productVersion': {'type': 'string', 'name': 'productVersion', 'native': True}})
        self.pendingAsset = pendingAsset
        self.Asset = Asset
        self.version = version
        self.productVersion = productVersion 
