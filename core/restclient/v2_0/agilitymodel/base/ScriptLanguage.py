from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class ScriptLanguageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, domain=None, variableRegex=None, editorMode=None, interpreter=None, type=None, operatingSystem=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'domain': {'type': 'Link', 'name': 'domain', 'minOccurs': '0', 'native': False}, 'editorMode': {'type': 'string', 'name': 'editorMode', 'minOccurs': '0', 'native': True}, 'variableRegex': {'type': 'string', 'name': 'variableRegex', 'minOccurs': '0', 'native': True}, 'interpreter': {'type': 'string', 'name': 'interpreter', 'minOccurs': '0', 'native': True}, 'type': {'type': 'ScriptType', 'name': 'type', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'operatingSystem', 'minOccurs': '0', 'native': True}})
        self.domain = domain
        self.variableRegex = variableRegex
        self.editorMode = editorMode
        self.interpreter = interpreter
        self.type = type
        self.operatingSystem = operatingSystem 
