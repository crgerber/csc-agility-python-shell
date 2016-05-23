from core.agility.v3_3.agilitymodel.base.Topology import TopologyBase
from core.agility.v3_3.agilitymodel.actions.Topology import TopologyActions

class Topology(TopologyBase, TopologyActions):
    '''
    classdocs
    '''
    def __init__(self, launcheraccessuri=[], accessuri=None, parentproject=None, fixedorder=[], anyorder=[], antiaffinity=None, mandatoryaffinity=None, stats=None, sourceblueprint=None, accessuriexpanded=None, blueprintsubcontainer=None, manualstartup=[], variables=[], resourceaffinity=None, aliases=[], deployer=[]):
        '''
        Constructor
        @param launcheraccessuri: launcheraccessuri minOccurs=0 maxOccurs=unbounded
        @type launcheraccessuri: AccessUri
        @param accessuri: accessuri minOccurs=0
        @type accessuri: string
        @param parentproject: parentproject minOccurs=0
        @type parentproject: Link
        @param fixedorder: fixedorder minOccurs=0 maxOccurs=unbounded
        @type fixedorder: Link
        @param anyorder: anyorder minOccurs=0 maxOccurs=unbounded
        @type anyorder: Link
        @param antiaffinity: antiaffinity minOccurs=0
        @type antiaffinity: boolean
        @param mandatoryaffinity: mandatoryaffinity minOccurs=0
        @type mandatoryaffinity: boolean
        @param stats: stats minOccurs=0
        @type stats: TopologyStats
        @param sourceblueprint: sourceblueprint minOccurs=0
        @type sourceblueprint: Link
        @param accessuriexpanded: accessuriexpanded minOccurs=0
        @type accessuriexpanded: string
        @param blueprintsubcontainer: blueprintsubcontainer minOccurs=0
        @type blueprintsubcontainer: boolean
        @param manualstartup: manualstartup minOccurs=0 maxOccurs=unbounded
        @type manualstartup: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param resourceaffinity: resourceaffinity
        @type resourceaffinity: ResourceAffinity
        @param aliases: aliases minOccurs=0 maxOccurs=unbounded
        @type aliases: Alias
        @param deployer: deployer minOccurs=0 maxOccurs=unbounded
        @type deployer: Link
        '''
        TopologyBase.__init__(self, launcheraccessuri=launcheraccessuri, accessuri=accessuri, parentproject=parentproject, fixedorder=fixedorder, anyorder=anyorder, antiaffinity=antiaffinity, mandatoryaffinity=mandatoryaffinity, stats=stats, sourceblueprint=sourceblueprint, accessuriexpanded=accessuriexpanded, blueprintsubcontainer=blueprintsubcontainer, manualstartup=manualstartup, variables=variables, resourceaffinity=resourceaffinity, aliases=aliases, deployer=deployer)
