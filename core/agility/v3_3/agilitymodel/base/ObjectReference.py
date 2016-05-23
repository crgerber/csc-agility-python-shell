from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ObjectReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, fieldassettypename=None, fieldname=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'fieldAssetTypeName': {'name': 'fieldassettypename', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'fieldName': {'name': 'fieldname', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.fieldassettypename = fieldassettypename
        self.fieldname = fieldname 
