from core.agility.v3_3.agilitymodel.base.Topology import TopologyBase
from core.agility.v3_3.agilitymodel.actions.Topology import TopologyActions

class Topology(TopologyBase, TopologyActions):
    '''
    classdocs
    '''
    def __init__(self, antiaffinity=None, stats=None, accessuri=None, accessuriexpanded=None, deployer=[], mandatoryaffinity=None, variables=[], blueprintsubcontainer=None, manualstartup=[], resourceaffinity=None, parentproject=None, sourceblueprint=None, fixedorder=[], launcheraccessuri=[], anyorder=[], aliases=[]):
        '''
        Constructor
        @param antiaffinity: antiaffinity minOccurs=0
        @type antiaffinity: boolean
        @param stats: stats minOccurs=0
        @type stats: TopologyStats
        @param accessuri: accessuri minOccurs=0
        @type accessuri: string
        @param accessuriexpanded: accessuriexpanded minOccurs=0
        @type accessuriexpanded: string
        @param deployer: deployer minOccurs=0 maxOccurs=unbounded
        @type deployer: Link
        @param mandatoryaffinity: mandatoryaffinity minOccurs=0
        @type mandatoryaffinity: boolean
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param blueprintsubcontainer: blueprintsubcontainer minOccurs=0
        @type blueprintsubcontainer: boolean
        @param manualstartup: manualstartup minOccurs=0 maxOccurs=unbounded
        @type manualstartup: Link
        @param resourceaffinity: resourceaffinity
        @type resourceaffinity: ResourceAffinity
        @param parentproject: parentproject minOccurs=0
        @type parentproject: Link
        @param sourceblueprint: sourceblueprint minOccurs=0
        @type sourceblueprint: Link
        @param fixedorder: fixedorder minOccurs=0 maxOccurs=unbounded
        @type fixedorder: Link
        @param launcheraccessuri: launcheraccessuri minOccurs=0 maxOccurs=unbounded
        @type launcheraccessuri: AccessUri
        @param anyorder: anyorder minOccurs=0 maxOccurs=unbounded
        @type anyorder: Link
        @param aliases: aliases minOccurs=0 maxOccurs=unbounded
        @type aliases: Alias
        '''
        TopologyBase.__init__(self, antiaffinity=antiaffinity, stats=stats, accessuri=accessuri, accessuriexpanded=accessuriexpanded, deployer=deployer, mandatoryaffinity=mandatoryaffinity, variables=variables, blueprintsubcontainer=blueprintsubcontainer, manualstartup=manualstartup, resourceaffinity=resourceaffinity, parentproject=parentproject, sourceblueprint=sourceblueprint, fixedorder=fixedorder, launcheraccessuri=launcheraccessuri, anyorder=anyorder, aliases=aliases)
