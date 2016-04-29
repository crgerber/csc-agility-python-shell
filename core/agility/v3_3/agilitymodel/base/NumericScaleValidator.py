from core.agility.v3_3.agilitymodel.base.FieldValidator import FieldValidatorBase

class NumericScaleValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, maxfractions=None, maxdigits=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'maxFractions': {'native': True, 'name': 'maxfractions', 'minOccurs': '0', 'type': 'int'}, 'maxDigits': {'native': True, 'name': 'maxdigits', 'minOccurs': '0', 'type': 'int'}})
        self.maxfractions = maxfractions
        self.maxdigits = maxdigits 
