from core.agility.common.AgilityModelBase import AgilityModelBase

class ControlBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, path='', name='', description='', allowedcontexts='', id=None, drilldowncontext=None, type='', properties=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'name': 'type', 'native': True, 'type': 'string'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'description': {'name': 'description', 'native': True, 'type': 'string'}, 'allowedContexts': {'name': 'allowedcontexts', 'native': True, 'type': 'string'}, 'path': {'name': 'path', 'native': True, 'type': 'string'}, 'drillDownContext': {'name': 'drilldowncontext', 'minOccurs': '0', 'native': False, 'type': 'PageContext'}, 'id': {'name': 'id', 'native': True, 'type': 'int'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.path = path
        self.name = name
        self.description = description
        self.allowedcontexts = allowedcontexts
        self.id = id
        self.drilldowncontext = drilldowncontext
        self.type = type
        self.properties = properties 
