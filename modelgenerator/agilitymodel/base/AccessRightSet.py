from AgilityModelBase import AgilityModelBase

class AccessRightSetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, filter=None, description=None, accessRight=list(), id=None, name=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'filter': {'type': 'string', 'name': 'filter', 'minOccurs': '0', 'native': True}, 'accessRight': {'maxOccurs': 'unbounded', 'type': 'AccessRight', 'name': 'accessRight', 'minOccurs': '0', 'native': False}, 'description': {'type': 'string', 'name': 'description', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}})
        self.filter = filter
        self.description = description
        self.accessRight = accessRight
        self.id = id
        self.name = name 
