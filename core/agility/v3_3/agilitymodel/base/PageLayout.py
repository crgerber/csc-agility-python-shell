from core.agility.common.AgilityModelBase import AgilityModelBase

class PageLayoutBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, path='', groups=[], name='', description='', id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'groups': {'maxOccurs': 'unbounded', 'native': False, 'name': 'groups', 'minOccurs': '0', 'type': 'PageLayoutGroup'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'path': {'native': True, 'name': 'path', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}})
        self.path = path
        self.groups = groups
        self.name = name
        self.description = description
        self.id = id 
