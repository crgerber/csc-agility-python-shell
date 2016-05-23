from core.agility.common.AgilityModelBase import AgilityModelBase

class VariableValueSetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, value=[], valuesource=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'value': {'name': 'value', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'valueSource': {'name': 'valuesource', 'minOccurs': '0', 'native': False, 'type': 'Asset'}})
        self.value = value
        self.valuesource = valuesource 
