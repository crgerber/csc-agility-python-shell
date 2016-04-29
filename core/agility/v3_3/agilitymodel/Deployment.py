from core.agility.v3_3.agilitymodel.base.Deployment import DeploymentBase
from core.agility.v3_3.agilitymodel.actions.Deployment import DeploymentActions

class Deployment(DeploymentBase, DeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, submitter=None, configuration=None, environment=None, deploymentbindings=[], releaseid=None, sourcedeployment=None, releaselabel=None, readyforpromotion=None, submitcomment=None, state=None, variables=[]):
        '''
        Constructor
        @param submitter: submitter minOccurs=0
        @type submitter: Link
        @param configuration: configuration minOccurs=0
        @type configuration: DeploymentConfiguration
        @param environment: environment minOccurs=0
        @type environment: Link
        @param deploymentbindings: deploymentbindings minOccurs=0 maxOccurs=unbounded
        @type deploymentbindings: DeploymentBinding
        @param releaseid: releaseid minOccurs=0
        @type releaseid: string
        @param sourcedeployment: sourcedeployment minOccurs=0
        @type sourcedeployment: Link
        @param releaselabel: releaselabel minOccurs=0
        @type releaselabel: string
        @param readyforpromotion: readyforpromotion minOccurs=0
        @type readyforpromotion: boolean
        @param submitcomment: submitcomment minOccurs=0
        @type submitcomment: string
        @param state: state minOccurs=0
        @type state: DeploymentState
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        '''
        DeploymentBase.__init__(self, submitter=submitter, configuration=configuration, environment=environment, deploymentbindings=deploymentbindings, releaseid=releaseid, sourcedeployment=sourcedeployment, releaselabel=releaselabel, readyforpromotion=readyforpromotion, submitcomment=submitcomment, state=state, variables=variables)
