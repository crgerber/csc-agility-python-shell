from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class GetRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, type='', id=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'string', 'name': 'type', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.type = type
        self.id = id 
