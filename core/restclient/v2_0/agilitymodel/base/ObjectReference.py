from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class ObjectReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, fieldName=None, fieldAssetTypeName=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'fieldName': {'type': 'string', 'name': 'fieldName', 'minOccurs': '0', 'native': True}, 'fieldAssetTypeName': {'type': 'string', 'name': 'fieldAssetTypeName', 'minOccurs': '0', 'native': True}})
        self.fieldName = fieldName
        self.fieldAssetTypeName = fieldAssetTypeName 
