from core.agility.v3_3.agilitymodel.base.FieldValidator import FieldValidatorBase

class DateValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, direction=[]):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'direction': {'maxOccurs': 'unbounded', 'native': False, 'name': 'direction', 'minOccurs': '0', 'type': 'DateDirection'}})
        self.direction = direction 
