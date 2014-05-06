from core.agility.common.AgilityModelBase import AgilityModelBase


class AuthTokenBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, token=None, id=None, created=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'token': {'type': 'string', 'name': 'token', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'created': {'type': 'dateTime', 'name': 'created', 'minOccurs': '0', 'native': True}})
        self.token = token
        self.id = id
        self.created = created 
