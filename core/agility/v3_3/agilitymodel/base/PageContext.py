from core.agility.common.AgilityModelBase import AgilityModelBase

class PageContextBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', type='', description='', id=None, pagelinks=[], routes=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'name': 'description', 'native': True, 'type': 'string'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}, 'pageLinks': {'name': 'pagelinks', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'routes': {'name': 'routes', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'id': {'name': 'id', 'native': True, 'type': 'int'}})
        self.name = name
        self.type = type
        self.description = description
        self.id = id
        self.pagelinks = pagelinks
        self.routes = routes 
