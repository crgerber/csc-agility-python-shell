from core.agility.v2_0.agilitymodel.base.FieldValidator import FieldValidatorBase

class StringLengthValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, minLength=None, maxLength=None):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'minLength': {'type': 'int', 'name': 'minLength', 'minOccurs': '0', 'native': True}, 'maxLength': {'type': 'int', 'name': 'maxLength', 'minOccurs': '0', 'native': True}})
        self.minLength = minLength
        self.maxLength = maxLength 
