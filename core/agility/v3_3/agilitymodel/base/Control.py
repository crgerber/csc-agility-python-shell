from core.agility.common.AgilityModelBase import AgilityModelBase

class ControlBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, drilldowncontext=None, properties=[], description='', name='', path='', type='', id=None, allowedcontexts=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'drillDownContext': {'type': 'PageContext', 'name': 'drilldowncontext', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'path': {'type': 'string', 'name': 'path', 'native': True}, 'allowedContexts': {'type': 'string', 'name': 'allowedcontexts', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'description': {'type': 'string', 'name': 'description', 'native': True}})
        self.drilldowncontext = drilldowncontext
        self.properties = properties
        self.description = description
        self.name = name
        self.path = path
        self.type = type
        self.id = id
        self.allowedcontexts = allowedcontexts 
