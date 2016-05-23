from core.agility.v3_3.agilitymodel.base.FieldValidator import FieldValidatorBase

class StringLengthValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, minlength=None, maxlength=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'minLength': {'name': 'minlength', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'maxLength': {'name': 'maxlength', 'minOccurs': '0', 'native': True, 'type': 'int'}})
        self.minlength = minlength
        self.maxlength = maxlength 
