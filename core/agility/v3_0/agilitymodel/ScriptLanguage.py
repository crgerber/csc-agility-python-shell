from core.agility.v3_0.agilitymodel.base.ScriptLanguage import ScriptLanguageBase
from core.agility.v3_0.agilitymodel.actions.ScriptLanguage import ScriptLanguageActions

class ScriptLanguage(ScriptLanguageBase, ScriptLanguageActions):
    '''
    classdocs
    '''
    def __init__(self, domain=None, variableregex=None, editormode=None, interpreter=None, type=None, operatingsystem=[]):
        '''
        Constructor
        @param domain: domain minOccurs=0
        @type domain: Link
        @param variableregex: variableregex minOccurs=0
        @type variableregex: string
        @param editormode: editormode minOccurs=0
        @type editormode: string
        @param interpreter: interpreter minOccurs=0
        @type interpreter: string
        @param type: type minOccurs=0
        @type type: ScriptType
        @param operatingsystem: operatingsystem minOccurs=0 maxOccurs=unbounded
        @type operatingsystem: string
        '''
        ScriptLanguageBase.__init__(self, domain=domain, variableregex=variableregex, editormode=editormode, interpreter=interpreter, type=type, operatingsystem=operatingsystem)
