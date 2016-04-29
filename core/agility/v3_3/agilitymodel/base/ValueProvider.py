from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ValueProviderBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, classname=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'classname': {'native': True, 'name': 'classname', 'minOccurs': '0', 'type': 'string'}})
        self.displayname = displayname
        self.classname = classname 
