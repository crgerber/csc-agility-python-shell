from core.agility.v3_3.agilitymodel.base.DesignContainer import DesignContainerBase
from core.agility.v3_3.agilitymodel.actions.DesignContainer import DesignContainerActions

class DesignContainer(DesignContainerBase, DesignContainerActions):
    '''
    classdocs
    '''
    def __init__(self, resourceaffinity=None, launcheraccessuri=[], anyorderitem=[], deep=False, antiaffinity=None, mandatoryaffinity=None, manualorderitem=[], aliases=[], deployers=[], fixedorderitem=[]):
        '''
        Constructor
        @param resourceaffinity: resourceaffinity
        @type resourceaffinity: ResourceAffinity
        @param launcheraccessuri: launcheraccessuri minOccurs=0 maxOccurs=unbounded
        @type launcheraccessuri: AccessUri
        @param anyorderitem: anyorderitem minOccurs=0 maxOccurs=unbounded
        @type anyorderitem: DesignItem
        @param deep: deep
        @type deep: boolean
        @param antiaffinity: antiaffinity minOccurs=0
        @type antiaffinity: boolean
        @param mandatoryaffinity: mandatoryaffinity minOccurs=0
        @type mandatoryaffinity: boolean
        @param manualorderitem: manualorderitem minOccurs=0 maxOccurs=unbounded
        @type manualorderitem: DesignItem
        @param aliases: aliases minOccurs=0 maxOccurs=unbounded
        @type aliases: DesignAlias
        @param deployers: deployers minOccurs=0 maxOccurs=unbounded
        @type deployers: DesignDeployer
        @param fixedorderitem: fixedorderitem minOccurs=0 maxOccurs=unbounded
        @type fixedorderitem: DesignItem
        '''
        DesignContainerBase.__init__(self, resourceaffinity=resourceaffinity, launcheraccessuri=launcheraccessuri, anyorderitem=anyorderitem, deep=deep, antiaffinity=antiaffinity, mandatoryaffinity=mandatoryaffinity, manualorderitem=manualorderitem, aliases=aliases, deployers=deployers, fixedorderitem=fixedorderitem)
