from core.agility.common.AgilityModelBase import AgilityModelBase

class AccessRightSetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, name=None, accessright=[], filter=None, description=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'accessRight': {'name': 'accessright', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AccessRight'}, 'filter': {'name': 'filter', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'description': {'name': 'description', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.id = id
        self.name = name
        self.accessright = accessright
        self.filter = filter
        self.description = description 
