from core.agility.v3_3.agilitymodel.base.DeploymentArtifactConfig import DeploymentArtifactConfigBase
from core.agility.v3_3.agilitymodel.actions.DeploymentArtifactConfig import DeploymentArtifactConfigActions

class DeploymentArtifactConfig(DeploymentArtifactConfigBase, DeploymentArtifactConfigActions):
    '''
    classdocs
    '''
    def __init__(self, artifact=None, artifacttype=None, properties=[], services=[], id=None, variables=[]):
        '''
        Constructor
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param services: services minOccurs=0 maxOccurs=unbounded
        @type services: string
        @param id: id
        @type id: int
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        '''
        DeploymentArtifactConfigBase.__init__(self, artifact=artifact, artifacttype=artifacttype, properties=properties, services=services, id=id, variables=variables)
