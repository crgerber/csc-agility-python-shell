from core.agility.common.AgilityModelBase import AgilityModelBase

class AccessRightSetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, accessright=[], name=None, description=None, id=None, filter=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'accessRight': {'maxOccurs': 'unbounded', 'native': False, 'name': 'accessright', 'minOccurs': '0', 'type': 'AccessRight'}, 'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'description': {'native': True, 'name': 'description', 'minOccurs': '0', 'type': 'string'}, 'filter': {'native': True, 'name': 'filter', 'minOccurs': '0', 'type': 'string'}})
        self.accessright = accessright
        self.name = name
        self.description = description
        self.id = id
        self.filter = filter 
