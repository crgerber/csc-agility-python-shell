from core.agility.common.AgilityModelBase import AgilityModelBase

class ProjectCreateRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, properties=[], location=None, name='', projecttemplate=None, description=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'projectTemplate': {'type': 'Link', 'name': 'projecttemplate', 'native': False}, 'description': {'type': 'string', 'name': 'description', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'location': {'type': 'Link', 'name': 'location', 'native': False}})
        self.properties = properties
        self.location = location
        self.name = name
        self.projecttemplate = projecttemplate
        self.description = description 
