from core.agility.v3_3.agilitymodel.base.DeploymentBinding import DeploymentBindingBase
from core.agility.v3_3.agilitymodel.actions.DeploymentBinding import DeploymentBindingActions

class DeploymentBinding(DeploymentBindingBase, DeploymentBindingActions):
    '''
    classdocs
    '''
    def __init__(self, platformservice=None, deployer=None, artifact=None, artifacturl=None, deploymentid='', id=None):
        '''
        Constructor
        @param platformservice: platformservice minOccurs=0
        @type platformservice: Link
        @param deployer: deployer minOccurs=0
        @type deployer: Link
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        @param artifacturl: artifacturl minOccurs=0
        @type artifacturl: string
        @param deploymentid: deploymentid
        @type deploymentid: string
        @param id: id
        @type id: int
        '''
        DeploymentBindingBase.__init__(self, platformservice=platformservice, deployer=deployer, artifact=artifact, artifacturl=artifacturl, deploymentid=deploymentid, id=id)
