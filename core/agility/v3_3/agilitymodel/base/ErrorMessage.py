from core.agility.common.AgilityModelBase import AgilityModelBase

class ErrorMessageBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, message='', code='', iserror=False, detail=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'message': {'name': 'message', 'native': True, 'type': 'string'}, 'code': {'name': 'code', 'native': True, 'type': 'string'}, 'isError': {'name': 'iserror', 'native': True, 'type': 'boolean'}, 'detail': {'name': 'detail', 'native': True, 'type': 'string'}})
        self.message = message
        self.code = code
        self.iserror = iserror
        self.detail = detail 
