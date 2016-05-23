from core.agility.v3_3.agilitymodel.base.ScriptLanguage import ScriptLanguageBase
from core.agility.v3_3.agilitymodel.actions.ScriptLanguage import ScriptLanguageActions

class ScriptLanguage(ScriptLanguageBase, ScriptLanguageActions):
    '''
    classdocs
    '''
    def __init__(self, operatingsystem=[], interpreter=None, editormode=None, domain=None, type=None, variableregex=None):
        '''
        Constructor
        @param operatingsystem: operatingsystem minOccurs=0 maxOccurs=unbounded
        @type operatingsystem: string
        @param interpreter: interpreter minOccurs=0
        @type interpreter: string
        @param editormode: editormode minOccurs=0
        @type editormode: string
        @param domain: domain minOccurs=0
        @type domain: Link
        @param type: type minOccurs=0
        @type type: ScriptType
        @param variableregex: variableregex minOccurs=0
        @type variableregex: string
        '''
        ScriptLanguageBase.__init__(self, operatingsystem=operatingsystem, interpreter=interpreter, editormode=editormode, domain=domain, type=type, variableregex=variableregex)
