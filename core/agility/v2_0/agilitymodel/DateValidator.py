from core.agility.v2_0.agilitymodel.base.DateValidator import DateValidatorBase
from core.agility.v2_0.agilitymodel.actions.DateValidator import DateValidatorActions

class DateValidator(DateValidatorBase, DateValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, direction=list()):
        '''
        Constructor
        @param direction: direction minOccurs=0 maxOccurs=unbounded
        @type direction: DateDirection
        '''
        DateValidatorBase.__init__(self, direction=direction)
