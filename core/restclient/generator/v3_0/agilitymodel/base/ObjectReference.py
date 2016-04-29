from .Asset import AssetBase

class ObjectReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, fieldname=None, fieldassettypename=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'fieldName': {'type': 'string', 'name': 'fieldname', 'minOccurs': '0', 'native': True}, 'fieldAssetTypeName': {'type': 'string', 'name': 'fieldassettypename', 'minOccurs': '0', 'native': True}})
        self.fieldname = fieldname
        self.fieldassettypename = fieldassettypename 
