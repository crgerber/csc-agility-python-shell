from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class GetRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, type=''):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'native': True, 'type': 'int'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}})
        self.id = id
        self.type = type 
