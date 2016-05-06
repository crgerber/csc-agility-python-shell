from core.agility.v3_3.agilitymodel.base.Deployment import DeploymentBase
from core.agility.v3_3.agilitymodel.actions.Deployment import DeploymentActions

class Deployment(DeploymentBase, DeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, environment=None, deploymentbindings=[], sourcedeployment=None, releaselabel=None, submitcomment=None, readyforpromotion=None, releaseid=None, state=None, submitter=None, configuration=None, variables=[]):
        '''
        Constructor
        @param environment: environment minOccurs=0
        @type environment: Link
        @param deploymentbindings: deploymentbindings minOccurs=0 maxOccurs=unbounded
        @type deploymentbindings: DeploymentBinding
        @param sourcedeployment: sourcedeployment minOccurs=0
        @type sourcedeployment: Link
        @param releaselabel: releaselabel minOccurs=0
        @type releaselabel: string
        @param submitcomment: submitcomment minOccurs=0
        @type submitcomment: string
        @param readyforpromotion: readyforpromotion minOccurs=0
        @type readyforpromotion: boolean
        @param releaseid: releaseid minOccurs=0
        @type releaseid: string
        @param state: state minOccurs=0
        @type state: DeploymentState
        @param submitter: submitter minOccurs=0
        @type submitter: Link
        @param configuration: configuration minOccurs=0
        @type configuration: DeploymentConfiguration
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        '''
        DeploymentBase.__init__(self, environment=environment, deploymentbindings=deploymentbindings, sourcedeployment=sourcedeployment, releaselabel=releaselabel, submitcomment=submitcomment, readyforpromotion=readyforpromotion, releaseid=releaseid, state=state, submitter=submitter, configuration=configuration, variables=variables)
