from core.agility.v3_0.agilitymodel.base.FieldValidator import FieldValidatorBase

class NumericScaleValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, maxdigits=None, maxfractions=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'maxDigits': {'type': 'int', 'name': 'maxdigits', 'minOccurs': '0', 'native': True}, 'maxFractions': {'type': 'int', 'name': 'maxfractions', 'minOccurs': '0', 'native': True}})
        self.maxdigits = maxdigits
        self.maxfractions = maxfractions 
