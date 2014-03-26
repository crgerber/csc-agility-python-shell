from core.agility.v2_0.agilitymodel.base.CloudMetaModel import CloudMetaModelBase
from core.agility.v2_0.agilitymodel.actions.CloudMetaModel import CloudMetaModelActions

class CloudMetaModel(CloudMetaModelBase, CloudMetaModelActions):
    '''
    classdocs
    '''
    def __init__(self, onboardMeta=list()):
        '''
        Constructor
        @param onboardMeta: onboardMeta minOccurs=0 maxOccurs=unbounded
        @type onboardMeta: OnboardMeta
        '''
        CloudMetaModelBase.__init__(self, onboardMeta=onboardMeta)
