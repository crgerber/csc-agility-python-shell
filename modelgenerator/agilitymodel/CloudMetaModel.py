from base.CloudMetaModel import CloudMetaModelBase
from actions.CloudMetaModel import CloudMetaModelActions

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
