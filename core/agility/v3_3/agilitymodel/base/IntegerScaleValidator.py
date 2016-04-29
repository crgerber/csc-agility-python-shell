from core.agility.v3_3.agilitymodel.base.FieldValidator import FieldValidatorBase

class IntegerScaleValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, maxdigits=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'maxDigits': {'native': True, 'name': 'maxdigits', 'type': 'int'}})
        self.maxdigits = maxdigits 
