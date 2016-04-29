from core.agility.common.AgilityModelBase import AgilityModelBase

class VariableValueSetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, valuesource=None, value=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'valueSource': {'native': False, 'name': 'valuesource', 'minOccurs': '0', 'type': 'Asset'}, 'value': {'maxOccurs': 'unbounded', 'native': False, 'name': 'value', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.valuesource = valuesource
        self.value = value 
