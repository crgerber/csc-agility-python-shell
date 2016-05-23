from core.agility.v3_3.agilitymodel.base.FieldValidator import FieldValidatorBase

class IntegerRangeValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, range=[]):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'range': {'name': 'range', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'IntegerRange'}})
        self.range = range 
