from core.agility.common.AgilityModelBase import AgilityModelBase

class PageLayoutBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', groups=[], path='', description=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'description': {'name': 'description', 'native': True, 'type': 'string'}, 'path': {'name': 'path', 'native': True, 'type': 'string'}, 'groups': {'name': 'groups', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PageLayoutGroup'}})
        self.id = id
        self.name = name
        self.groups = groups
        self.path = path
        self.description = description 
