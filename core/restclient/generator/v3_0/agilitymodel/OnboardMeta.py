from .base.OnboardMeta import OnboardMetaBase
from .actions.OnboardMeta import OnboardMetaActions

class OnboardMeta(OnboardMetaBase, OnboardMetaActions):
    '''
    classdocs
    '''
    def __init__(self, type='', supportedinstancefield=[]):
        '''
        Constructor
        @param type: type
        @type type: string
        @param supportedinstancefield: supportedinstancefield minOccurs=0 maxOccurs=unbounded
        @type supportedinstancefield: FieldMeta
        '''
        OnboardMetaBase.__init__(self, type=type, supportedinstancefield=supportedinstancefield)
