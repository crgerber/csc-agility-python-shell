from core.agility.v3_3.agilitymodel.base.DeploymentArtifactConfig import DeploymentArtifactConfigBase
from core.agility.v3_3.agilitymodel.actions.DeploymentArtifactConfig import DeploymentArtifactConfigActions

class DeploymentArtifactConfig(DeploymentArtifactConfigBase, DeploymentArtifactConfigActions):
    '''
    classdocs
    '''
    def __init__(self, variables=[], artifact=None, id=None, services=[], artifacttype=None, properties=[]):
        '''
        Constructor
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        @param id: id
        @type id: int
        @param services: services minOccurs=0 maxOccurs=unbounded
        @type services: string
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        DeploymentArtifactConfigBase.__init__(self, variables=variables, artifact=artifact, id=id, services=services, artifacttype=artifacttype, properties=properties)
