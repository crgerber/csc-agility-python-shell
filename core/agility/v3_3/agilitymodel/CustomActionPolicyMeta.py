from base.CustomActionPolicyMeta import CustomActionPolicyMetaBase
from actions.CustomActionPolicyMeta import CustomActionPolicyMetaActions

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
