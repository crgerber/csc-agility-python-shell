from base.DeploymentArtifactConfig import DeploymentArtifactConfigBase
from actions.DeploymentArtifactConfig import DeploymentArtifactConfigActions

class DeploymentArtifactConfig(DeploymentArtifactConfigBase, DeploymentArtifactConfigActions):
    '''
    classdocs
    '''
    def __init__(self, variables=list(), artifact=None, properties=list(), services=list(), artifactType=None, id=None):
        '''
        Constructor
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param services: services minOccurs=0 maxOccurs=unbounded
        @type services: string
        @param artifactType: artifactType minOccurs=0
        @type artifactType: Link
        @param id: id
        @type id: int
        '''
        DeploymentArtifactConfigBase.__init__(self, variables=variables, artifact=artifact, properties=properties, services=services, artifactType=artifactType, id=id)
