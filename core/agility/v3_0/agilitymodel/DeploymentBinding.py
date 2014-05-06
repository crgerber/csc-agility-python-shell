from core.agility.v3_0.agilitymodel.base.DeploymentBinding import DeploymentBindingBase
from core.agility.v3_0.agilitymodel.actions.DeploymentBinding import DeploymentBindingActions

class DeploymentBinding(DeploymentBindingBase, DeploymentBindingActions):
    '''
    classdocs
    '''
    def __init__(self, deployer=None, deploymentid='', artifact=None, artifacturl=None, platformservice=None, id=None):
        '''
        Constructor
        @param deployer: deployer minOccurs=0
        @type deployer: Link
        @param deploymentid: deploymentid
        @type deploymentid: string
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        @param artifacturl: artifacturl minOccurs=0
        @type artifacturl: string
        @param platformservice: platformservice minOccurs=0
        @type platformservice: Link
        @param id: id
        @type id: int
        '''
        DeploymentBindingBase.__init__(self, deployer=deployer, deploymentid=deploymentid, artifact=artifact, artifacturl=artifacturl, platformservice=platformservice, id=id)
