from core.agility.common.AgilityModelBase import AgilityModelBase

class StoreResourceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', value='', type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'value': {'name': 'value', 'native': True, 'type': 'string'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}})
        self.id = id
        self.name = name
        self.value = value
        self.type = type 
