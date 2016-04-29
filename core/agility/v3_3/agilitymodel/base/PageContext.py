from core.agility.common.AgilityModelBase import AgilityModelBase

class PageContextBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', description='', pagelinks=[], routes=[], id=None, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'routes': {'maxOccurs': 'unbounded', 'native': False, 'name': 'routes', 'minOccurs': '0', 'type': 'AssetProperty'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'pageLinks': {'maxOccurs': 'unbounded', 'native': False, 'name': 'pagelinks', 'minOccurs': '0', 'type': 'Link'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.name = name
        self.description = description
        self.pagelinks = pagelinks
        self.routes = routes
        self.id = id
        self.type = type 
