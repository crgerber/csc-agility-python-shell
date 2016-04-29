from core.agility.v3_3.agilitymodel.base.FieldValidator import FieldValidatorBase

class RegexValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, expression=[]):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'expression': {'maxOccurs': 'unbounded', 'native': True, 'name': 'expression', 'minOccurs': '0', 'type': 'string'}})
        self.expression = expression 
