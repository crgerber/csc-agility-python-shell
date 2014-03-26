from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class PropertyBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, availableOptions=list(), encrypted=False, overridable=False, value='', data=None, dataEncrypted=False):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'dataEncrypted': {'type': 'boolean', 'name': 'dataEncrypted', 'native': True}, 'encrypted': {'type': 'boolean', 'name': 'encrypted', 'native': True}, 'overridable': {'type': 'boolean', 'name': 'overridable', 'native': True}, 'value': {'type': 'string', 'name': 'value', 'native': True}, 'data': {'type': 'hexBinary', 'name': 'data', 'minOccurs': '0', 'native': True}, 'availableOptions': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'availableOptions', 'minOccurs': '0', 'native': True}})
        self.availableOptions = availableOptions
        self.encrypted = encrypted
        self.overridable = overridable
        self.value = value
        self.data = data
        self.dataEncrypted = dataEncrypted 
