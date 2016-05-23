from core.agility.v3_3.agilitymodel.base.DesignContainer import DesignContainerBase
from core.agility.v3_3.agilitymodel.actions.DesignContainer import DesignContainerActions

class DesignContainer(DesignContainerBase, DesignContainerActions):
    '''
    classdocs
    '''
    def __init__(self, anyorderitem=[], antiaffinity=None, deep=False, manualorderitem=[], fixedorderitem=[], resourceaffinity=None, mandatoryaffinity=None, aliases=[], deployers=[], launcheraccessuri=[]):
        '''
        Constructor
        @param anyorderitem: anyorderitem minOccurs=0 maxOccurs=unbounded
        @type anyorderitem: DesignItem
        @param antiaffinity: antiaffinity minOccurs=0
        @type antiaffinity: boolean
        @param deep: deep
        @type deep: boolean
        @param manualorderitem: manualorderitem minOccurs=0 maxOccurs=unbounded
        @type manualorderitem: DesignItem
        @param fixedorderitem: fixedorderitem minOccurs=0 maxOccurs=unbounded
        @type fixedorderitem: DesignItem
        @param resourceaffinity: resourceaffinity
        @type resourceaffinity: ResourceAffinity
        @param mandatoryaffinity: mandatoryaffinity minOccurs=0
        @type mandatoryaffinity: boolean
        @param aliases: aliases minOccurs=0 maxOccurs=unbounded
        @type aliases: DesignAlias
        @param deployers: deployers minOccurs=0 maxOccurs=unbounded
        @type deployers: DesignDeployer
        @param launcheraccessuri: launcheraccessuri minOccurs=0 maxOccurs=unbounded
        @type launcheraccessuri: AccessUri
        '''
        DesignContainerBase.__init__(self, anyorderitem=anyorderitem, antiaffinity=antiaffinity, deep=deep, manualorderitem=manualorderitem, fixedorderitem=fixedorderitem, resourceaffinity=resourceaffinity, mandatoryaffinity=mandatoryaffinity, aliases=aliases, deployers=deployers, launcheraccessuri=launcheraccessuri)
