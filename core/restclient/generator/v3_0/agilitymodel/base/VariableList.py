from AgilityModelBase import AgilityModelBase

class VariableListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, variable=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variable': {'maxOccurs': 'unbounded', 'type': 'Variable', 'name': 'variable', 'minOccurs': '0', 'native': False}})
        self.variable = variable 
