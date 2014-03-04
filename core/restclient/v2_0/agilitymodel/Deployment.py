from core.restclient.v2_0.agilitymodel.base.Deployment import DeploymentBase
from core.restclient.v2_0.agilitymodel.actions.Deployment import DeploymentActions

class Deployment(DeploymentBase, DeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, environment=None, deploymentBindings=list(), sourceDeployment=None, releaseLabel=None, submitComment=None, readyForPromotion=None, releaseId=None, state=None, submitter=None, configuration=None, variables=list()):
        '''
        Constructor
        @param environment: environment minOccurs=0
        @type environment: Link
        @param deploymentBindings: deploymentBindings minOccurs=0 maxOccurs=unbounded
        @type deploymentBindings: DeploymentBinding
        @param sourceDeployment: sourceDeployment minOccurs=0
        @type sourceDeployment: Link
        @param releaseLabel: releaseLabel minOccurs=0
        @type releaseLabel: string
        @param submitComment: submitComment minOccurs=0
        @type submitComment: string
        @param readyForPromotion: readyForPromotion minOccurs=0
        @type readyForPromotion: boolean
        @param releaseId: releaseId minOccurs=0
        @type releaseId: string
        @param state: state minOccurs=0
        @type state: DeploymentState
        @param submitter: submitter minOccurs=0
        @type submitter: Link
        @param configuration: configuration minOccurs=0
        @type configuration: DeploymentConfiguration
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        '''
        DeploymentBase.__init__(self, environment=environment, deploymentBindings=deploymentBindings, sourceDeployment=sourceDeployment, releaseLabel=releaseLabel, submitComment=submitComment, readyForPromotion=readyForPromotion, releaseId=releaseId, state=state, submitter=submitter, configuration=configuration, variables=variables)
