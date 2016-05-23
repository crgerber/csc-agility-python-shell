from core.agility.v3_3.agilitymodel.base.DeploymentBinding import DeploymentBindingBase
from core.agility.v3_3.agilitymodel.actions.DeploymentBinding import DeploymentBindingActions

class DeploymentBinding(DeploymentBindingBase, DeploymentBindingActions):
    '''
    classdocs
    '''
    def __init__(self, artifact=None, id=None, artifacturl=None, platformservice=None, deployer=None, deploymentid=''):
        '''
        Constructor
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        @param id: id
        @type id: int
        @param artifacturl: artifacturl minOccurs=0
        @type artifacturl: string
        @param platformservice: platformservice minOccurs=0
        @type platformservice: Link
        @param deployer: deployer minOccurs=0
        @type deployer: Link
        @param deploymentid: deploymentid
        @type deploymentid: string
        '''
        DeploymentBindingBase.__init__(self, artifact=artifact, id=id, artifacturl=artifacturl, platformservice=platformservice, deployer=deployer, deploymentid=deploymentid)
