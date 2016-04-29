from .base.DesignContainer import DesignContainerBase
from .actions.DesignContainer import DesignContainerActions

class DesignContainer(DesignContainerBase, DesignContainerActions):
    '''
    classdocs
    '''
    def __init__(self, antiaffinity=None, resourceaffinity=None, fixedorderitem=[], deep=False, anyorderitem=[], manualorderitem=[], deployers=[], mandatoryaffinity=None, launcheraccessuri=[], aliases=[]):
        '''
        Constructor
        @param antiaffinity: antiaffinity minOccurs=0
        @type antiaffinity: boolean
        @param resourceaffinity: resourceaffinity
        @type resourceaffinity: ResourceAffinity
        @param fixedorderitem: fixedorderitem minOccurs=0 maxOccurs=unbounded
        @type fixedorderitem: DesignItem
        @param deep: deep
        @type deep: boolean
        @param anyorderitem: anyorderitem minOccurs=0 maxOccurs=unbounded
        @type anyorderitem: DesignItem
        @param manualorderitem: manualorderitem minOccurs=0 maxOccurs=unbounded
        @type manualorderitem: DesignItem
        @param deployers: deployers minOccurs=0 maxOccurs=unbounded
        @type deployers: DesignDeployer
        @param mandatoryaffinity: mandatoryaffinity minOccurs=0
        @type mandatoryaffinity: boolean
        @param launcheraccessuri: launcheraccessuri minOccurs=0 maxOccurs=unbounded
        @type launcheraccessuri: AccessUri
        @param aliases: aliases minOccurs=0 maxOccurs=unbounded
        @type aliases: DesignAlias
        '''
        DesignContainerBase.__init__(self, antiaffinity=antiaffinity, resourceaffinity=resourceaffinity, fixedorderitem=fixedorderitem, deep=deep, anyorderitem=anyorderitem, manualorderitem=manualorderitem, deployers=deployers, mandatoryaffinity=mandatoryaffinity, launcheraccessuri=launcheraccessuri, aliases=aliases)
