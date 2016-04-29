from .base.CloudMetaModel import CloudMetaModelBase
from .actions.CloudMetaModel import CloudMetaModelActions

class CloudMetaModel(CloudMetaModelBase, CloudMetaModelActions):
    '''
    classdocs
    '''
    def __init__(self, onboardmeta=[]):
        '''
        Constructor
        @param onboardmeta: onboardmeta minOccurs=0 maxOccurs=unbounded
        @type onboardmeta: OnboardMeta
        '''
        CloudMetaModelBase.__init__(self, onboardmeta=onboardmeta)
