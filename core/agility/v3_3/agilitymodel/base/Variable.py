from core.agility.v3_3.agilitymodel.base.AssetProperty import AssetPropertyBase

class VariableBase(AssetPropertyBase):
    '''
    classdocs
    '''
    def __init__(self, value=None):
        AssetPropertyBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'value': {'native': True, 'name': 'value', 'minOccurs': '0', 'type': 'string'}})
        self.value = value 
