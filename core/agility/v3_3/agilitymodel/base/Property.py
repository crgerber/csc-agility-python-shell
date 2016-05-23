from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, value='', data=None, dataencrypted=False, encrypted=False, overridable=False, availableoptions=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'value': {'name': 'value', 'native': True, 'type': 'string'}, 'data': {'name': 'data', 'minOccurs': '0', 'native': True, 'type': 'hexBinary'}, 'encrypted': {'name': 'encrypted', 'native': True, 'type': 'boolean'}, 'dataEncrypted': {'name': 'dataencrypted', 'native': True, 'type': 'boolean'}, 'overridable': {'name': 'overridable', 'native': True, 'type': 'boolean'}, 'availableOptions': {'name': 'availableoptions', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}})
        self.value = value
        self.data = data
        self.dataencrypted = dataencrypted
        self.encrypted = encrypted
        self.overridable = overridable
        self.availableoptions = availableoptions 
