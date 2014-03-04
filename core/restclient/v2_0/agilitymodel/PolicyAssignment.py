from core.restclient.v2_0.agilitymodel.base.PolicyAssignment import PolicyAssignmentBase
from core.restclient.v2_0.agilitymodel.actions.PolicyAssignment import PolicyAssignmentActions

class PolicyAssignment(PolicyAssignmentBase, PolicyAssignmentActions):
    '''
    classdocs
    '''
    def __init__(self, itemId=None, itemClass=None, policyTypeName=None, inherited=None, permissioned=None, applyChildrenDepth=None, allowChildrenOverride=False, policy=None, filterMatch=None, itemName=None, applyToSelf=False):
        '''
        Constructor
        @param itemId: itemId minOccurs=0
        @type itemId: int
        @param itemClass: itemClass minOccurs=0
        @type itemClass: string
        @param policyTypeName: policyTypeName minOccurs=0
        @type policyTypeName: string
        @param inherited: inherited minOccurs=0
        @type inherited: boolean
        @param permissioned: permissioned minOccurs=0
        @type permissioned: boolean
        @param applyChildrenDepth: applyChildrenDepth minOccurs=0
        @type applyChildrenDepth: int
        @param allowChildrenOverride: allowChildrenOverride
        @type allowChildrenOverride: boolean
        @param policy: policy minOccurs=0
        @type policy: Link
        @param filterMatch: filterMatch minOccurs=0
        @type filterMatch: boolean
        @param itemName: itemName minOccurs=0
        @type itemName: string
        @param applyToSelf: applyToSelf
        @type applyToSelf: boolean
        '''
        PolicyAssignmentBase.__init__(self, itemId=itemId, itemClass=itemClass, policyTypeName=policyTypeName, inherited=inherited, permissioned=permissioned, applyChildrenDepth=applyChildrenDepth, allowChildrenOverride=allowChildrenOverride, policy=policy, filterMatch=filterMatch, itemName=itemName, applyToSelf=applyToSelf)
