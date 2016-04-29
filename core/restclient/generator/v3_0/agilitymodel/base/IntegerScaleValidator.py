from .FieldValidator import FieldValidatorBase

class IntegerScaleValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, maxdigits=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'maxDigits': {'type': 'int', 'name': 'maxdigits', 'native': True}})
        self.maxdigits = maxdigits 
