from core.agility.v3_3.agilitymodel.base.CustomActionPolicyMeta import CustomActionPolicyMetaBase
from core.agility.v3_3.agilitymodel.actions.CustomActionPolicyMeta import CustomActionPolicyMetaActions

class CustomActionPolicyMeta(CustomActionPolicyMetaBase, CustomActionPolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, supportedassettype=[]):
        '''
        Constructor
        @param supportedassettype: supportedassettype minOccurs=0 maxOccurs=unbounded
        @type supportedassettype: AssetTypeMeta
        '''
        CustomActionPolicyMetaBase.__init__(self, supportedassettype=supportedassettype)
