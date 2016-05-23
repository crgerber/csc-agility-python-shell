from core.agility.v3_3.agilitymodel.base.FieldValidator import FieldValidatorBase

class NumericScaleValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, maxdigits=None, maxfractions=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'maxDigits': {'name': 'maxdigits', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'maxFractions': {'name': 'maxfractions', 'minOccurs': '0', 'native': True, 'type': 'int'}})
        self.maxdigits = maxdigits
        self.maxfractions = maxfractions 
