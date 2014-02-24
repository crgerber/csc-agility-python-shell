from base.PolicyMetaModel import PolicyMetaModelBase
from actions.PolicyMetaModel import PolicyMetaModelActions

class PolicyMetaModel(PolicyMetaModelBase, PolicyMetaModelActions):
    '''
    classdocs
    '''
    def __init__(self, policyMeta=list()):
        '''
        Constructor
        @param policyMeta: policyMeta minOccurs=0 maxOccurs=unbounded
        @type policyMeta: PolicyMeta
        '''
        PolicyMetaModelBase.__init__(self, policyMeta=policyMeta)
