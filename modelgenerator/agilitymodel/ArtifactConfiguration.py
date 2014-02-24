from base.ArtifactConfiguration import ArtifactConfigurationBase
from actions.ArtifactConfiguration import ArtifactConfigurationActions

class ArtifactConfiguration(ArtifactConfigurationBase, ArtifactConfigurationActions):
    '''
    classdocs
    '''
    def __init__(self, runtimeBindings=list(), variables=list(), id=None):
        '''
        Constructor
        @param runtimeBindings: runtimeBindings minOccurs=0 maxOccurs=unbounded
        @type runtimeBindings: ArtifactRuntimeBinding
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param id: id
        @type id: int
        '''
        ArtifactConfigurationBase.__init__(self, runtimeBindings=runtimeBindings, variables=variables, id=id)
