from ApiRequest import ApiRequestBase

class SearchRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, type=''):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'string', 'name': 'type', 'native': True}})
        self.type = type 
