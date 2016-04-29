from .FieldValidator import FieldValidatorBase

class DateValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, direction=[]):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'direction': {'maxOccurs': 'unbounded', 'type': 'DateDirection', 'name': 'direction', 'minOccurs': '0', 'native': False}})
        self.direction = direction 
