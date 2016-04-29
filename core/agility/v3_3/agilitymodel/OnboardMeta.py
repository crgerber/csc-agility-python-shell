from core.agility.v3_3.agilitymodel.base.OnboardMeta import OnboardMetaBase
from core.agility.v3_3.agilitymodel.actions.OnboardMeta import OnboardMetaActions

class OnboardMeta(OnboardMetaBase, OnboardMetaActions):
    '''
    classdocs
    '''
    def __init__(self, supportedinstancefield=[], type=''):
        '''
        Constructor
        @param supportedinstancefield: supportedinstancefield minOccurs=0 maxOccurs=unbounded
        @type supportedinstancefield: FieldMeta
        @param type: type
        @type type: string
        '''
        OnboardMetaBase.__init__(self, supportedinstancefield=supportedinstancefield, type=type)
