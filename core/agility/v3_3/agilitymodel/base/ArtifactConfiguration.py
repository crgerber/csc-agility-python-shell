from core.agility.common.AgilityModelBase import AgilityModelBase

class ArtifactConfigurationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, variables=[], runtimebindings=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'native': True, 'type': 'int'}, 'runtimeBindings': {'name': 'runtimebindings', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ArtifactRuntimeBinding'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.id = id
        self.variables = variables
        self.runtimebindings = runtimebindings 
