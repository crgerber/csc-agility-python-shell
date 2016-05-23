from core.agility.common.AgilityModelBase import AgilityModelBase

class AuthTokenBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, token=None, created=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'token': {'name': 'token', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'created': {'name': 'created', 'minOccurs': '0', 'native': True, 'type': 'dateTime'}})
        self.id = id
        self.token = token
        self.created = created 
