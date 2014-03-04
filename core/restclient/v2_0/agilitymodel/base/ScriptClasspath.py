from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class ScriptClasspathBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, path='', unerasable=False, domain=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'type': 'string', 'name': 'path', 'native': True}, 'unerasable': {'type': 'boolean', 'name': 'unerasable', 'native': True}, 'domain': {'type': 'Link', 'name': 'domain', 'minOccurs': '0', 'native': False}})
        self.path = path
        self.unerasable = unerasable
        self.domain = domain 
