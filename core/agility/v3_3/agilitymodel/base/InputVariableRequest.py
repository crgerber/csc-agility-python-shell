from core.agility.common.AgilityModelBase import AgilityModelBase

class InputVariableRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, variablesource=[], excludepackagescripts=False, valuesource=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variableSource': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'variablesource', 'minOccurs': '0', 'native': False}, 'valueSource': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'valuesource', 'minOccurs': '0', 'native': False}, 'excludePackageScripts': {'type': 'boolean', 'name': 'excludepackagescripts', 'native': True}})
        self.variablesource = variablesource
        self.excludepackagescripts = excludepackagescripts
        self.valuesource = valuesource 
