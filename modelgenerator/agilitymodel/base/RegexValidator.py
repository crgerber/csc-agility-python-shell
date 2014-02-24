from FieldValidator import FieldValidatorBase

class RegexValidatorBase(FieldValidatorBase):
    '''
    classdocs
    '''
    def __init__(self, expression=list()):
        FieldValidatorBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'expression': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'expression', 'minOccurs': '0', 'native': True}})
        self.expression = expression 
