from .base.DeploymentArtifactConfig import DeploymentArtifactConfigBase
from .actions.DeploymentArtifactConfig import DeploymentArtifactConfigActions

class DeploymentArtifactConfig(DeploymentArtifactConfigBase, DeploymentArtifactConfigActions):
    '''
    classdocs
    '''
    def __init__(self, variables=[], artifact=None, properties=[], services=[], artifacttype=None, id=None):
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
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: Link
        @param id: id
        @type id: int
        '''
        DeploymentArtifactConfigBase.__init__(self, variables=variables, artifact=artifact, properties=properties, services=services, artifacttype=artifacttype, id=id)
