from core.agility.v3_3.agilitymodel.base.FieldValidator import FieldValidatorBase

class StringLengthValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, maxlength=None, minlength=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'minLength': {'native': True, 'name': 'minlength', 'minOccurs': '0', 'type': 'int'}, 'maxLength': {'native': True, 'name': 'maxlength', 'minOccurs': '0', 'type': 'int'}})
        self.maxlength = maxlength
        self.minlength = minlength 
