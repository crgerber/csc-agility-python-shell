from core.agility.common.AgilityModelBase import AgilityModelBase

class EnvelopeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, pendingasset=[], asset=[], version='', productversion=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'pendingAsset': {'maxOccurs': 'unbounded', 'type': 'Asset', 'name': 'pendingasset', 'minOccurs': '0', 'native': False}, 'Asset': {'maxOccurs': 'unbounded', 'type': 'Asset', 'name': 'asset', 'minOccurs': '0', 'native': False}, 'version': {'type': 'string', 'name': 'version', 'native': True}, 'productVersion': {'type': 'string', 'name': 'productversion', 'native': True}})
        self.pendingasset = pendingasset
        self.asset = asset
        self.version = version
        self.productversion = productversion 
