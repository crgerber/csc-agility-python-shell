from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ScriptLanguageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, editormode=None, domain=None, operatingsystem=[], variableregex=None, interpreter=None, type=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'editorMode': {'native': True, 'name': 'editormode', 'minOccurs': '0', 'type': 'string'}, 'domain': {'native': False, 'name': 'domain', 'minOccurs': '0', 'type': 'Link'}, 'operatingSystem': {'maxOccurs': 'unbounded', 'native': True, 'name': 'operatingsystem', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'ScriptType'}, 'interpreter': {'native': True, 'name': 'interpreter', 'minOccurs': '0', 'type': 'string'}, 'variableRegex': {'native': True, 'name': 'variableregex', 'minOccurs': '0', 'type': 'string'}})
        self.editormode = editormode
        self.domain = domain
        self.operatingsystem = operatingsystem
        self.variableregex = variableregex
        self.interpreter = interpreter
        self.type = type 
