from core.agility.v3_3.agilitymodel.base.OnboardMeta import OnboardMetaBase
from core.agility.v3_3.agilitymodel.actions.OnboardMeta import OnboardMetaActions

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
