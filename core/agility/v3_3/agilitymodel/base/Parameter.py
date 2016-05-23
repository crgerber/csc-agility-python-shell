from core.agility.common.AgilityModelBase import AgilityModelBase

class ParameterBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', value=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'value': {'name': 'value', 'native': True, 'type': 'string'}})
        self.name = name
        self.value = value 
