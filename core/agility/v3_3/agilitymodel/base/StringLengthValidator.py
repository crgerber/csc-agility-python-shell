from core.agility.v3_3.agilitymodel.base.FieldValidator import FieldValidatorBase

class StringLengthValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, minlength=None, maxlength=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'minLength': {'type': 'int', 'name': 'minlength', 'minOccurs': '0', 'native': True}, 'maxLength': {'type': 'int', 'name': 'maxlength', 'minOccurs': '0', 'native': True}})
        self.minlength = minlength
        self.maxlength = maxlength 
