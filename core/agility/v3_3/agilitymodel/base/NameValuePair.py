from core.agility.common.AgilityModelBase import AgilityModelBase

class NameValuePairBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', value=None, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'type': 'string'}, 'value': {'native': True, 'name': 'value', 'minOccurs': '0', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}})
        self.name = name
        self.value = value
        self.id = id 
