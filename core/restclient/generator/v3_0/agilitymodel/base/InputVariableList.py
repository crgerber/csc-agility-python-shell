from AgilityModelBase import AgilityModelBase

class InputVariableListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, inputvariable=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'inputVariable': {'maxOccurs': 'unbounded', 'type': 'InputVariable', 'name': 'inputvariable', 'minOccurs': '0', 'native': False}})
        self.inputvariable = inputvariable 
