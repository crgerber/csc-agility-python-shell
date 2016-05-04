from Asset import AssetBase

class ValueProviderBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, classname=None, displayname=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'classname': {'type': 'string', 'name': 'classname', 'minOccurs': '0', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}})
        self.classname = classname
        self.displayname = displayname 
