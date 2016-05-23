from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ScriptLanguageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, operatingsystem=[], interpreter=None, editormode=None, domain=None, type=None, variableregex=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'operatingSystem': {'name': 'operatingsystem', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'interpreter': {'name': 'interpreter', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'editorMode': {'name': 'editormode', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'domain': {'name': 'domain', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': False, 'type': 'ScriptType'}, 'variableRegex': {'name': 'variableregex', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.operatingsystem = operatingsystem
        self.interpreter = interpreter
        self.editormode = editormode
        self.domain = domain
        self.type = type
        self.variableregex = variableregex 
