from core.agility.common.AgilityModelBase import AgilityModelBase

class InputVariableRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, valuesource=[], variablesource=[], excludepackagescripts=False):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'valueSource': {'maxOccurs': 'unbounded', 'native': False, 'name': 'valuesource', 'minOccurs': '0', 'type': 'Link'}, 'variableSource': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variablesource', 'minOccurs': '0', 'type': 'Link'}, 'excludePackageScripts': {'native': True, 'name': 'excludepackagescripts', 'type': 'boolean'}})
        self.valuesource = valuesource
        self.variablesource = variablesource
        self.excludepackagescripts = excludepackagescripts 
