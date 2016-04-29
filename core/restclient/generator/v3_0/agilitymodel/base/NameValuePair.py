from .AgilityModelBase import AgilityModelBase

class NameValuePairBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, value=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'value': {'type': 'string', 'name': 'value', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.id = id
        self.value = value
        self.name = name 
