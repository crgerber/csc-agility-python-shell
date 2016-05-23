from core.agility.common.AgilityModelBase import AgilityModelBase

class EnvelopeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, productversion='', pendingasset=[], version='', asset=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'pendingAsset': {'name': 'pendingasset', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Asset'}, 'version': {'name': 'version', 'native': True, 'type': 'string'}, 'Asset': {'name': 'asset', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Asset'}, 'productVersion': {'name': 'productversion', 'native': True, 'type': 'string'}})
        self.productversion = productversion
        self.pendingasset = pendingasset
        self.version = version
        self.asset = asset 
