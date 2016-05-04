from core.agility.common.AgilityModelBase import AgilityModelBase

class PageContextBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, description='', pagelinks=[], routes=[], type='', id=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'type': 'string', 'name': 'description', 'native': True}, 'pageLinks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'pagelinks', 'minOccurs': '0', 'native': False}, 'routes': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'routes', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.description = description
        self.pagelinks = pagelinks
        self.routes = routes
        self.type = type
        self.id = id
        self.name = name 
