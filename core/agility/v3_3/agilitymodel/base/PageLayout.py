from core.agility.common.AgilityModelBase import AgilityModelBase

class PageLayoutBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, path='', description='', id=None, groups=[], name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'type': 'string', 'name': 'path', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'native': True}, 'groups': {'maxOccurs': 'unbounded', 'type': 'PageLayoutGroup', 'name': 'groups', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.path = path
        self.description = description
        self.id = id
        self.groups = groups
        self.name = name 
