from core.agility.v3_3.agilitymodel.base.CloudMetaModel import CloudMetaModelBase
from core.agility.v3_3.agilitymodel.actions.CloudMetaModel import CloudMetaModelActions

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
