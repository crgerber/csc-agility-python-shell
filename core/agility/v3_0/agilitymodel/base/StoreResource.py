from core.agility.common.AgilityModelBase import AgilityModelBase


class StoreResourceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, type='', id=None, value='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'string', 'name': 'type', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'value': {'type': 'string', 'name': 'value', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.type = type
        self.id = id
        self.value = value
        self.name = name 
