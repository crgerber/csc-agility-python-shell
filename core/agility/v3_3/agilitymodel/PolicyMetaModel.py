from core.agility.v3_3.agilitymodel.base.PolicyMetaModel import PolicyMetaModelBase
from core.agility.v3_3.agilitymodel.actions.PolicyMetaModel import PolicyMetaModelActions

class PolicyMetaModel(PolicyMetaModelBase, PolicyMetaModelActions):
    '''
    classdocs
    '''
    def __init__(self, policymeta=[]):
        '''
        Constructor
        @param policymeta: policymeta minOccurs=0 maxOccurs=unbounded
        @type policymeta: PolicyMeta
        '''
        PolicyMetaModelBase.__init__(self, policymeta=policymeta)
