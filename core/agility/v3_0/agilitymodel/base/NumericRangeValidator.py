from core.agility.v3_0.agilitymodel.base.FieldValidator import FieldValidatorBase

class NumericRangeValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, range=[]):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'range': {'maxOccurs': 'unbounded', 'type': 'NumericRange', 'name': 'range', 'minOccurs': '0', 'native': False}})
        self.range = range 
