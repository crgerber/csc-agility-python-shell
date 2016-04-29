from core.agility.common.AgilityModelBase import AgilityModelBase

class ProjectCreateRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, projecttemplate=None, location=None, name='', description=None, properties=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'projectTemplate': {'native': False, 'name': 'projecttemplate', 'type': 'Link'}, 'location': {'native': False, 'name': 'location', 'type': 'Link'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'description': {'native': True, 'name': 'description', 'minOccurs': '0', 'type': 'string'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.projecttemplate = projecttemplate
        self.location = location
        self.name = name
        self.description = description
        self.properties = properties 
