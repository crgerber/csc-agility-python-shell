from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ValueProviderBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, classname=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'classname': {'name': 'classname', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.displayname = displayname
        self.classname = classname 
