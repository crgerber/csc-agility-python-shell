from FieldValidator import FieldValidatorBase

class NumericScaleValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, maxDigits=None, maxFractions=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'maxDigits': {'type': 'int', 'name': 'maxDigits', 'minOccurs': '0', 'native': True}, 'maxFractions': {'type': 'int', 'name': 'maxFractions', 'minOccurs': '0', 'native': True}})
        self.maxDigits = maxDigits
        self.maxFractions = maxFractions 
