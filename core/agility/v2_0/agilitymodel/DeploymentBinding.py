from core.agility.v2_0.agilitymodel.base.DeploymentBinding import DeploymentBindingBase
from core.agility.v2_0.agilitymodel.actions.DeploymentBinding import DeploymentBindingActions

class DeploymentBinding(DeploymentBindingBase, DeploymentBindingActions):
    '''
    classdocs
    '''
    def __init__(self, deployer=None, deploymentId='', artifact=None, artifactUrl=None, platformService=None, id=None):
        '''
        Constructor
        @param deployer: deployer minOccurs=0
        @type deployer: Link
        @param deploymentId: deploymentId
        @type deploymentId: string
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        @param artifactUrl: artifactUrl minOccurs=0
        @type artifactUrl: string
        @param platformService: platformService minOccurs=0
        @type platformService: Link
        @param id: id
        @type id: int
        '''
        DeploymentBindingBase.__init__(self, deployer=deployer, deploymentId=deploymentId, artifact=artifact, artifactUrl=artifactUrl, platformService=platformService, id=id)
