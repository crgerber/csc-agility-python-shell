from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class ListRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, type=''):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.type = type 
