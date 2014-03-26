from core.agility.v2_0.agilitymodel.base.FieldValidator import FieldValidatorBase

class IntegerRangeValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, range=list()):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'range': {'maxOccurs': 'unbounded', 'type': 'IntegerRange', 'name': 'range', 'minOccurs': '0', 'native': False}})
        self.range = range 
