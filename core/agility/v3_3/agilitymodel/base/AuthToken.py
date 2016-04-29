from core.agility.common.AgilityModelBase import AgilityModelBase

class AuthTokenBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, token=None, id=None, created=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'token': {'native': True, 'name': 'token', 'minOccurs': '0', 'type': 'string'}, 'created': {'native': True, 'name': 'created', 'minOccurs': '0', 'type': 'dateTime'}})
        self.token = token
        self.id = id
        self.created = created 
