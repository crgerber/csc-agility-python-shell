from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class PropertyMatchBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, matches='', name='', value=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'matches': {'type': 'string', 'name': 'matches', 'native': True}, 'name': {'use': 'required', 'type': 'string', 'name': 'name', 'native': True}, 'value': {'type': 'string', 'name': 'value', 'native': True}})
        self.matches = matches
        self.name = name
        self.value = value 
