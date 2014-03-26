from core.agility.v2_0.agilitymodel.base.PolicyMetaModel import PolicyMetaModelBase
from core.agility.v2_0.agilitymodel.actions.PolicyMetaModel import PolicyMetaModelActions

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
