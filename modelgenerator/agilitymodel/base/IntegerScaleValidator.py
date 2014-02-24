from FieldValidator import FieldValidatorBase

class IntegerScaleValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, maxDigits=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'maxDigits': {'type': 'int', 'name': 'maxDigits', 'native': True}})
        self.maxDigits = maxDigits 
