from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class CreateRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, asset=None, parent=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'asset': {'type': 'Asset', 'name': 'asset', 'native': False}, 'parent': {'type': 'Asset', 'name': 'parent', 'minOccurs': '0', 'native': False}})
        self.asset = asset
        self.parent = parent 
