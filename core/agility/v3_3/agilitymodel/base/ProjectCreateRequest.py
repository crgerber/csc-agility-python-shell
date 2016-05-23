from core.agility.common.AgilityModelBase import AgilityModelBase

class ProjectCreateRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', description=None, projecttemplate=None, location=None, properties=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'description': {'name': 'description', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'projectTemplate': {'name': 'projecttemplate', 'native': False, 'type': 'Link'}, 'location': {'name': 'location', 'native': False, 'type': 'Link'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.name = name
        self.description = description
        self.projecttemplate = projecttemplate
        self.location = location
        self.properties = properties 
