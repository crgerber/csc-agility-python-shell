from core.agility.common.AgilityModelBase import AgilityModelBase

class ErrorMessageBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, message='', code='', iserror=False, detail=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'message': {'native': True, 'name': 'message', 'type': 'string'}, 'code': {'native': True, 'name': 'code', 'type': 'string'}, 'isError': {'native': True, 'name': 'iserror', 'type': 'boolean'}, 'detail': {'native': True, 'name': 'detail', 'type': 'string'}})
        self.message = message
        self.code = code
        self.iserror = iserror
        self.detail = detail 
