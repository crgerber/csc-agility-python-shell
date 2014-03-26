from core.agility.v2_0.agilitymodel.base.DesignContainer import DesignContainerBase
from core.agility.v2_0.agilitymodel.actions.DesignContainer import DesignContainerActions

class DesignContainer(DesignContainerBase, DesignContainerActions):
    '''
    classdocs
    '''
    def __init__(self, antiAffinity=None, resourceAffinity=None, fixedOrderItem=list(), deep=False, anyOrderItem=list(), manualOrderItem=list(), deployers=list(), mandatoryAffinity=None, launcherAccessUri=list(), aliases=list()):
        '''
        Constructor
        @param antiAffinity: antiAffinity minOccurs=0
        @type antiAffinity: boolean
        @param resourceAffinity: resourceAffinity
        @type resourceAffinity: ResourceAffinity
        @param fixedOrderItem: fixedOrderItem minOccurs=0 maxOccurs=unbounded
        @type fixedOrderItem: DesignItem
        @param deep: deep
        @type deep: boolean
        @param anyOrderItem: anyOrderItem minOccurs=0 maxOccurs=unbounded
        @type anyOrderItem: DesignItem
        @param manualOrderItem: manualOrderItem minOccurs=0 maxOccurs=unbounded
        @type manualOrderItem: DesignItem
        @param deployers: deployers minOccurs=0 maxOccurs=unbounded
        @type deployers: DesignDeployer
        @param mandatoryAffinity: mandatoryAffinity minOccurs=0
        @type mandatoryAffinity: boolean
        @param launcherAccessUri: launcherAccessUri minOccurs=0 maxOccurs=unbounded
        @type launcherAccessUri: AccessUri
        @param aliases: aliases minOccurs=0 maxOccurs=unbounded
        @type aliases: DesignAlias
        '''
        DesignContainerBase.__init__(self, antiAffinity=antiAffinity, resourceAffinity=resourceAffinity, fixedOrderItem=fixedOrderItem, deep=deep, anyOrderItem=anyOrderItem, manualOrderItem=manualOrderItem, deployers=deployers, mandatoryAffinity=mandatoryAffinity, launcherAccessUri=launcherAccessUri, aliases=aliases)
