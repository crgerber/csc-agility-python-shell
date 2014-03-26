from core.agility.v3_0.agilitymodel.base.LifecyclePolicyMeta import LifecyclePolicyMetaBase
from core.agility.v3_0.agilitymodel.actions.LifecyclePolicyMeta import LifecyclePolicyMetaActions

class LifecyclePolicyMeta(LifecyclePolicyMetaBase, LifecyclePolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, supportedassettype=[]):
        '''
        Constructor
        @param supportedassettype: supportedassettype minOccurs=0 maxOccurs=unbounded
        @type supportedassettype: AssetTypeMeta
        '''
        LifecyclePolicyMetaBase.__init__(self, supportedassettype=supportedassettype)
