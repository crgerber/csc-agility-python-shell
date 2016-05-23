from core.agility.v3_3.agilitymodel.base.Deployment import DeploymentBase
from core.agility.v3_3.agilitymodel.actions.Deployment import DeploymentActions

class Deployment(DeploymentBase, DeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, readyforpromotion=None, environment=None, state=None, sourcedeployment=None, submitter=None, deploymentbindings=[], releaselabel=None, configuration=None, submitcomment=None, variables=[], releaseid=None):
        '''
        Constructor
        @param readyforpromotion: readyforpromotion minOccurs=0
        @type readyforpromotion: boolean
        @param environment: environment minOccurs=0
        @type environment: Link
        @param state: state minOccurs=0
        @type state: DeploymentState
        @param sourcedeployment: sourcedeployment minOccurs=0
        @type sourcedeployment: Link
        @param submitter: submitter minOccurs=0
        @type submitter: Link
        @param deploymentbindings: deploymentbindings minOccurs=0 maxOccurs=unbounded
        @type deploymentbindings: DeploymentBinding
        @param releaselabel: releaselabel minOccurs=0
        @type releaselabel: string
        @param configuration: configuration minOccurs=0
        @type configuration: DeploymentConfiguration
        @param submitcomment: submitcomment minOccurs=0
        @type submitcomment: string
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param releaseid: releaseid minOccurs=0
        @type releaseid: string
        '''
        DeploymentBase.__init__(self, readyforpromotion=readyforpromotion, environment=environment, state=state, sourcedeployment=sourcedeployment, submitter=submitter, deploymentbindings=deploymentbindings, releaselabel=releaselabel, configuration=configuration, submitcomment=submitcomment, variables=variables, releaseid=releaseid)
