from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class CreateRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, asset=None, parent=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'asset': {'name': 'asset', 'native': False, 'type': 'Asset'}, 'parent': {'name': 'parent', 'minOccurs': '0', 'native': False, 'type': 'Asset'}})
        self.asset = asset
        self.parent = parent 
