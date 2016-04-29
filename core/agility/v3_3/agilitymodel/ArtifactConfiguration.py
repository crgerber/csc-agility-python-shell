from core.agility.v3_3.agilitymodel.base.ArtifactConfiguration import ArtifactConfigurationBase
from core.agility.v3_3.agilitymodel.actions.ArtifactConfiguration import ArtifactConfigurationActions

class ArtifactConfiguration(ArtifactConfigurationBase, ArtifactConfigurationActions):
    '''
    classdocs
    '''
    def __init__(self, variables=[], id=None, runtimebindings=[]):
        '''
        Constructor
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param id: id
        @type id: int
        @param runtimebindings: runtimebindings minOccurs=0 maxOccurs=unbounded
        @type runtimebindings: ArtifactRuntimeBinding
        '''
        ArtifactConfigurationBase.__init__(self, variables=variables, id=id, runtimebindings=runtimebindings)
