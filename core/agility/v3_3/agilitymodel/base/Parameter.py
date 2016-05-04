from core.agility.common.AgilityModelBase import AgilityModelBase

class ParameterBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', value=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'type': 'string', 'name': 'name', 'native': True}, 'value': {'type': 'string', 'name': 'value', 'native': True}})
        self.name = name
        self.value = value 
