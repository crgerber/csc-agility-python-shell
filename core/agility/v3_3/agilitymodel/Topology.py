from core.agility.v3_3.agilitymodel.base.Topology import TopologyBase
from core.agility.v3_3.agilitymodel.actions.Topology import TopologyActions

class Topology(TopologyBase, TopologyActions):
    '''
    classdocs
    '''
    def __init__(self, deployer=[], manualstartup=[], mandatoryaffinity=None, accessuriexpanded=None, sourceblueprint=None, launcheraccessuri=[], blueprintsubcontainer=None, antiaffinity=None, resourceaffinity=None, anyorder=[], stats=None, aliases=[], accessuri=None, fixedorder=[], parentproject=None, variables=[]):
        '''
        Constructor
        @param deployer: deployer minOccurs=0 maxOccurs=unbounded
        @type deployer: Link
        @param manualstartup: manualstartup minOccurs=0 maxOccurs=unbounded
        @type manualstartup: Link
        @param mandatoryaffinity: mandatoryaffinity minOccurs=0
        @type mandatoryaffinity: boolean
        @param accessuriexpanded: accessuriexpanded minOccurs=0
        @type accessuriexpanded: string
        @param sourceblueprint: sourceblueprint minOccurs=0
        @type sourceblueprint: Link
        @param launcheraccessuri: launcheraccessuri minOccurs=0 maxOccurs=unbounded
        @type launcheraccessuri: AccessUri
        @param blueprintsubcontainer: blueprintsubcontainer minOccurs=0
        @type blueprintsubcontainer: boolean
        @param antiaffinity: antiaffinity minOccurs=0
        @type antiaffinity: boolean
        @param resourceaffinity: resourceaffinity
        @type resourceaffinity: ResourceAffinity
        @param anyorder: anyorder minOccurs=0 maxOccurs=unbounded
        @type anyorder: Link
        @param stats: stats minOccurs=0
        @type stats: TopologyStats
        @param aliases: aliases minOccurs=0 maxOccurs=unbounded
        @type aliases: Alias
        @param accessuri: accessuri minOccurs=0
        @type accessuri: string
        @param fixedorder: fixedorder minOccurs=0 maxOccurs=unbounded
        @type fixedorder: Link
        @param parentproject: parentproject minOccurs=0
        @type parentproject: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        '''
        TopologyBase.__init__(self, deployer=deployer, manualstartup=manualstartup, mandatoryaffinity=mandatoryaffinity, accessuriexpanded=accessuriexpanded, sourceblueprint=sourceblueprint, launcheraccessuri=launcheraccessuri, blueprintsubcontainer=blueprintsubcontainer, antiaffinity=antiaffinity, resourceaffinity=resourceaffinity, anyorder=anyorder, stats=stats, aliases=aliases, accessuri=accessuri, fixedorder=fixedorder, parentproject=parentproject, variables=variables)
