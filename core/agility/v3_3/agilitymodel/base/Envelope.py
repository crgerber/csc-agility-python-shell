from core.agility.common.AgilityModelBase import AgilityModelBase

class EnvelopeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, version='', pendingasset=[], asset=[], productversion=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'version': {'native': True, 'name': 'version', 'type': 'string'}, 'pendingAsset': {'maxOccurs': 'unbounded', 'native': False, 'name': 'pendingasset', 'minOccurs': '0', 'type': 'Asset'}, 'Asset': {'maxOccurs': 'unbounded', 'native': False, 'name': 'asset', 'minOccurs': '0', 'type': 'Asset'}, 'productVersion': {'native': True, 'name': 'productversion', 'type': 'string'}})
        self.version = version
        self.pendingasset = pendingasset
        self.asset = asset
        self.productversion = productversion 
