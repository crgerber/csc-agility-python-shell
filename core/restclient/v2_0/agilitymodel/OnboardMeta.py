from core.restclient.v2_0.agilitymodel.base.OnboardMeta import OnboardMetaBase
from core.restclient.v2_0.agilitymodel.actions.OnboardMeta import OnboardMetaActions

class OnboardMeta(OnboardMetaBase, OnboardMetaActions):
    '''
    classdocs
    '''
    def __init__(self, type='', supportedInstanceField=list()):
        '''
        Constructor
        @param type: type
        @type type: string
        @param supportedInstanceField: supportedInstanceField minOccurs=0 maxOccurs=unbounded
        @type supportedInstanceField: FieldMeta
        '''
        OnboardMetaBase.__init__(self, type=type, supportedInstanceField=supportedInstanceField)
