from core.agility.common.AgilityModelBase import AgilityModelBase

class ErrorInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, message=None, level=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'message': {'name': 'message', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'level': {'name': 'level', 'minOccurs': '0', 'native': False, 'type': 'ErrorLevel'}})
        self.message = message
        self.level = level 
