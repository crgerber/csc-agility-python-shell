from core.agility.common.AgilityModelBase import AgilityModelBase

class StoreResourceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', value='', id=None, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'type': 'string'}, 'value': {'native': True, 'name': 'value', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.name = name
        self.value = value
        self.id = id
        self.type = type 
