from .AgilityModelBase import AgilityModelBase

class ErrorMessageBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, message='', code='', detail='', iserror=False):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'message': {'type': 'string', 'name': 'message', 'native': True}, 'code': {'type': 'string', 'name': 'code', 'native': True}, 'detail': {'type': 'string', 'name': 'detail', 'native': True}, 'isError': {'type': 'boolean', 'name': 'iserror', 'native': True}})
        self.message = message
        self.code = code
        self.detail = detail
        self.iserror = iserror 
