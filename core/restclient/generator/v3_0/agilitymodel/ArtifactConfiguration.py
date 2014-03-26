from base.ArtifactConfiguration import ArtifactConfigurationBase
from actions.ArtifactConfiguration import ArtifactConfigurationActions

class ArtifactConfiguration(ArtifactConfigurationBase, ArtifactConfigurationActions):
    '''
    classdocs
    '''
    def __init__(self, runtimebindings=[], variables=[], id=None):
        '''
        Constructor
        @param runtimebindings: runtimebindings minOccurs=0 maxOccurs=unbounded
        @type runtimebindings: ArtifactRuntimeBinding
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param id: id
        @type id: int
        '''
        ArtifactConfigurationBase.__init__(self, runtimebindings=runtimebindings, variables=variables, id=id)
