from .AgilityModelBase import AgilityModelBase

class VariableValueSetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, value=[], valuesource=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'value': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'value', 'minOccurs': '0', 'native': False}, 'valueSource': {'type': 'Asset', 'name': 'valuesource', 'minOccurs': '0', 'native': False}})
        self.value = value
        self.valuesource = valuesource 
