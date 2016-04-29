from core.agility.common.AgilityModelBase import AgilityModelBase

class ArtifactConfigurationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, variables=[], id=None, runtimebindings=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'runtimeBindings': {'maxOccurs': 'unbounded', 'native': False, 'name': 'runtimebindings', 'minOccurs': '0', 'type': 'ArtifactRuntimeBinding'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.variables = variables
        self.id = id
        self.runtimebindings = runtimebindings 
