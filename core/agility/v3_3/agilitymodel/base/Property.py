from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, encrypted=False, dataencrypted=False, overridable=False, value='', data=None, availableoptions=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'encrypted': {'native': True, 'name': 'encrypted', 'type': 'boolean'}, 'dataEncrypted': {'native': True, 'name': 'dataencrypted', 'type': 'boolean'}, 'overridable': {'native': True, 'name': 'overridable', 'type': 'boolean'}, 'value': {'native': True, 'name': 'value', 'type': 'string'}, 'data': {'native': True, 'name': 'data', 'minOccurs': '0', 'type': 'hexBinary'}, 'availableOptions': {'maxOccurs': 'unbounded', 'native': True, 'name': 'availableoptions', 'minOccurs': '0', 'type': 'string'}})
        self.encrypted = encrypted
        self.dataencrypted = dataencrypted
        self.overridable = overridable
        self.value = value
        self.data = data
        self.availableoptions = availableoptions 
