from base.Topology import TopologyBase
from actions.Topology import TopologyActions

class Topology(TopologyBase, TopologyActions):
    '''
    classdocs
    '''
    def __init__(self, antiAffinity=None, accessUri=None, accessUriExpanded=None, deployer=list(), mandatoryAffinity=None, variables=list(), blueprintSubcontainer=None, manualStartup=list(), resourceAffinity=None, sourceBlueprint=None, fixedOrder=list(), launcherAccessUri=list(), anyOrder=list(), aliases=list()):
        '''
        Constructor
        @param antiAffinity: antiAffinity minOccurs=0
        @type antiAffinity: boolean
        @param accessUri: accessUri minOccurs=0
        @type accessUri: string
        @param accessUriExpanded: accessUriExpanded minOccurs=0
        @type accessUriExpanded: string
        @param deployer: deployer minOccurs=0 maxOccurs=unbounded
        @type deployer: Link
        @param mandatoryAffinity: mandatoryAffinity minOccurs=0
        @type mandatoryAffinity: boolean
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param blueprintSubcontainer: blueprintSubcontainer minOccurs=0
        @type blueprintSubcontainer: boolean
        @param manualStartup: manualStartup minOccurs=0 maxOccurs=unbounded
        @type manualStartup: Link
        @param resourceAffinity: resourceAffinity
        @type resourceAffinity: ResourceAffinity
        @param sourceBlueprint: sourceBlueprint minOccurs=0
        @type sourceBlueprint: Link
        @param fixedOrder: fixedOrder minOccurs=0 maxOccurs=unbounded
        @type fixedOrder: Link
        @param launcherAccessUri: launcherAccessUri minOccurs=0 maxOccurs=unbounded
        @type launcherAccessUri: AccessUri
        @param anyOrder: anyOrder minOccurs=0 maxOccurs=unbounded
        @type anyOrder: Link
        @param aliases: aliases minOccurs=0 maxOccurs=unbounded
        @type aliases: Alias
        '''
        TopologyBase.__init__(self, antiAffinity=antiAffinity, accessUri=accessUri, accessUriExpanded=accessUriExpanded, deployer=deployer, mandatoryAffinity=mandatoryAffinity, variables=variables, blueprintSubcontainer=blueprintSubcontainer, manualStartup=manualStartup, resourceAffinity=resourceAffinity, sourceBlueprint=sourceBlueprint, fixedOrder=fixedOrder, launcherAccessUri=launcherAccessUri, anyOrder=anyOrder, aliases=aliases)
