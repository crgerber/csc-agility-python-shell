from core.agility.common.AgilityModelBase import AgilityModelBase

class ErrorInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, message=None, level=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'message': {'native': True, 'name': 'message', 'minOccurs': '0', 'type': 'string'}, 'level': {'native': False, 'name': 'level', 'minOccurs': '0', 'type': 'ErrorLevel'}})
        self.message = message
        self.level = level 
