from core.agility.common.AgilityModelBase import AgilityModelBase

class NameValuePairBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', value=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'value': {'name': 'value', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.id = id
        self.name = name
        self.value = value 
