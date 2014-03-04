from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class ValueProviderBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, classname=None, displayName=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'classname': {'type': 'string', 'name': 'classname', 'minOccurs': '0', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}})
        self.classname = classname
        self.displayName = displayName 
