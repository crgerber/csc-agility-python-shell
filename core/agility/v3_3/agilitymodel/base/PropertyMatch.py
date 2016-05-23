from core.agility.common.AgilityModelBase import AgilityModelBase

class PropertyMatchBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', value='', matches=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string', 'use': 'required'}, 'value': {'name': 'value', 'native': True, 'type': 'string'}, 'matches': {'name': 'matches', 'native': True, 'type': 'string'}})
        self.name = name
        self.value = value
        self.matches = matches 
