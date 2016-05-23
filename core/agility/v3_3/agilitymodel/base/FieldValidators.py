from core.agility.common.AgilityModelBase import AgilityModelBase

class FieldValidatorsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, numericscalevalidator=None, emailvalidator=None, stringlengthvalidator=None, numericrangevalidator=None, integerscalevalidator=None, integerrangevalidator=None, regexvalidator=None, datevalidator=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'NumericScaleValidator': {'name': 'numericscalevalidator', 'native': False, 'type': 'NumericScaleValidator'}, 'EmailValidator': {'name': 'emailvalidator', 'native': False, 'type': 'EmailValidator'}, 'StringLengthValidator': {'name': 'stringlengthvalidator', 'native': False, 'type': 'StringLengthValidator'}, 'IntegerRangeValidator': {'name': 'integerrangevalidator', 'native': False, 'type': 'IntegerRangeValidator'}, 'IntegerScaleValidator': {'name': 'integerscalevalidator', 'native': False, 'type': 'IntegerScaleValidator'}, 'NumericRangeValidator': {'name': 'numericrangevalidator', 'native': False, 'type': 'NumericRangeValidator'}, 'DateValidator': {'name': 'datevalidator', 'native': False, 'type': 'DateValidator'}, 'RegexValidator': {'name': 'regexvalidator', 'native': False, 'type': 'RegexValidator'}})
        self.numericscalevalidator = numericscalevalidator
        self.emailvalidator = emailvalidator
        self.stringlengthvalidator = stringlengthvalidator
        self.numericrangevalidator = numericrangevalidator
        self.integerscalevalidator = integerscalevalidator
        self.integerrangevalidator = integerrangevalidator
        self.regexvalidator = regexvalidator
        self.datevalidator = datevalidator 
