from Asset import AssetBase

class ScriptLanguageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, domain=None, variableregex=None, editormode=None, interpreter=None, type=None, operatingsystem=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'domain': {'type': 'Link', 'name': 'domain', 'minOccurs': '0', 'native': False}, 'editorMode': {'type': 'string', 'name': 'editormode', 'minOccurs': '0', 'native': True}, 'variableRegex': {'type': 'string', 'name': 'variableregex', 'minOccurs': '0', 'native': True}, 'interpreter': {'type': 'string', 'name': 'interpreter', 'minOccurs': '0', 'native': True}, 'type': {'type': 'ScriptType', 'name': 'type', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'operatingsystem', 'minOccurs': '0', 'native': True}})
        self.domain = domain
        self.variableregex = variableregex
        self.editormode = editormode
        self.interpreter = interpreter
        self.type = type
        self.operatingsystem = operatingsystem 
