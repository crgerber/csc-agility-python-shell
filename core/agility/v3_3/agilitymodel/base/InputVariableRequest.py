from core.agility.common.AgilityModelBase import AgilityModelBase

class InputVariableRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, excludepackagescripts=False, variablesource=[], valuesource=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'excludePackageScripts': {'name': 'excludepackagescripts', 'native': True, 'type': 'boolean'}, 'variableSource': {'name': 'variablesource', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'valueSource': {'name': 'valuesource', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.excludepackagescripts = excludepackagescripts
        self.variablesource = variablesource
        self.valuesource = valuesource 
