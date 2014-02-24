from AssetProperty import AssetPropertyBase

class VariableBase(AssetPropertyBase):
    '''
    classdocs
    '''
    def __init__(self, value=None):
        AssetPropertyBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'value': {'type': 'string', 'name': 'value', 'minOccurs': '0', 'native': True}})
        self.value = value 
