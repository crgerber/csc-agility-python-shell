from core.agility.v3_3.agilitymodel.base.FieldValidators import FieldValidatorsBase
from core.agility.v3_3.agilitymodel.actions.FieldValidators import FieldValidatorsActions

class FieldValidators(FieldValidatorsBase, FieldValidatorsActions):
    '''
    classdocs
    '''
    def __init__(self, numericscalevalidator=None, emailvalidator=None, stringlengthvalidator=None, numericrangevalidator=None, integerscalevalidator=None, integerrangevalidator=None, regexvalidator=None, datevalidator=None):
        '''
        Constructor
        @param numericscalevalidator: numericscalevalidator
        @type numericscalevalidator: NumericScaleValidator
        @param emailvalidator: emailvalidator
        @type emailvalidator: EmailValidator
        @param stringlengthvalidator: stringlengthvalidator
        @type stringlengthvalidator: StringLengthValidator
        @param numericrangevalidator: numericrangevalidator
        @type numericrangevalidator: NumericRangeValidator
        @param integerscalevalidator: integerscalevalidator
        @type integerscalevalidator: IntegerScaleValidator
        @param integerrangevalidator: integerrangevalidator
        @type integerrangevalidator: IntegerRangeValidator
        @param regexvalidator: regexvalidator
        @type regexvalidator: RegexValidator
        @param datevalidator: datevalidator
        @type datevalidator: DateValidator
        '''
        FieldValidatorsBase.__init__(self, numericscalevalidator=numericscalevalidator, emailvalidator=emailvalidator, stringlengthvalidator=stringlengthvalidator, numericrangevalidator=numericrangevalidator, integerscalevalidator=integerscalevalidator, integerrangevalidator=integerrangevalidator, regexvalidator=regexvalidator, datevalidator=datevalidator)
