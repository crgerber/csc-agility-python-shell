from core.agility.common.AgilityModelBase import AgilityModelBase

class ControlBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, path='', properties=[], description='', allowedcontexts='', drilldowncontext=None, name='', id=None, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'native': True, 'name': 'path', 'type': 'string'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}, 'allowedContexts': {'native': True, 'name': 'allowedcontexts', 'type': 'string'}, 'drillDownContext': {'native': False, 'name': 'drilldowncontext', 'minOccurs': '0', 'type': 'PageContext'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'AssetProperty'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.path = path
        self.properties = properties
        self.description = description
        self.allowedcontexts = allowedcontexts
        self.drilldowncontext = drilldowncontext
        self.name = name
        self.id = id
        self.type = type 
