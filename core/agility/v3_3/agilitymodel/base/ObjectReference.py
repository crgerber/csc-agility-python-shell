from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ObjectReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, fieldname=None, fieldassettypename=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'fieldName': {'native': True, 'name': 'fieldname', 'minOccurs': '0', 'type': 'string'}, 'fieldAssetTypeName': {'native': True, 'name': 'fieldassettypename', 'minOccurs': '0', 'type': 'string'}})
        self.fieldname = fieldname
        self.fieldassettypename = fieldassettypename 
