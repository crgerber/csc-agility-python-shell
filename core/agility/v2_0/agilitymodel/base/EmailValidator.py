from core.agility.v2_0.agilitymodel.base.FieldValidator import FieldValidatorBase

class EmailValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
