from core.agility.v2_0.agilitymodel.base.ScriptLanguage import ScriptLanguageBase
from core.agility.v2_0.agilitymodel.actions.ScriptLanguage import ScriptLanguageActions

class ScriptLanguage(ScriptLanguageBase, ScriptLanguageActions):
    '''
    classdocs
    '''
    def __init__(self, domain=None, variableRegex=None, editorMode=None, interpreter=None, type=None, operatingSystem=list()):
        '''
        Constructor
        @param domain: domain minOccurs=0
        @type domain: Link
        @param variableRegex: variableRegex minOccurs=0
        @type variableRegex: string
        @param editorMode: editorMode minOccurs=0
        @type editorMode: string
        @param interpreter: interpreter minOccurs=0
        @type interpreter: string
        @param type: type minOccurs=0
        @type type: ScriptType
        @param operatingSystem: operatingSystem minOccurs=0 maxOccurs=unbounded
        @type operatingSystem: string
        '''
        ScriptLanguageBase.__init__(self, domain=domain, variableRegex=variableRegex, editorMode=editorMode, interpreter=interpreter, type=type, operatingSystem=operatingSystem)
