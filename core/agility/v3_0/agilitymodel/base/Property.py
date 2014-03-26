from core.agility.v3_0.agilitymodel.base.Asset import AssetBase

class PropertyBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, availableoptions=[], encrypted=False, overridable=False, value='', data=None, dataencrypted=False):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'dataEncrypted': {'type': 'boolean', 'name': 'dataencrypted', 'native': True}, 'encrypted': {'type': 'boolean', 'name': 'encrypted', 'native': True}, 'overridable': {'type': 'boolean', 'name': 'overridable', 'native': True}, 'value': {'type': 'string', 'name': 'value', 'native': True}, 'data': {'type': 'hexBinary', 'name': 'data', 'minOccurs': '0', 'native': True}, 'availableOptions': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'availableoptions', 'minOccurs': '0', 'native': True}})
        self.availableoptions = availableoptions
        self.encrypted = encrypted
        self.overridable = overridable
        self.value = value
        self.data = data
        self.dataencrypted = dataencrypted 
