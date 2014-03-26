from AgilityModelBase import AgilityModelBase

class ErrorInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, message=None, level=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'message': {'type': 'string', 'name': 'message', 'minOccurs': '0', 'native': True}, 'level': {'type': 'ErrorLevel', 'name': 'level', 'minOccurs': '0', 'native': False}})
        self.message = message
        self.level = level 
