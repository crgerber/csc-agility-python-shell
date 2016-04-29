from core.agility.common.AgilityModelBase import AgilityModelBase

class PropertyMatchBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, matches='', name='', value=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'use': 'required', 'type': 'string'}, 'matches': {'native': True, 'name': 'matches', 'type': 'string'}, 'value': {'native': True, 'name': 'value', 'type': 'string'}})
        self.matches = matches
        self.name = name
        self.value = value 
