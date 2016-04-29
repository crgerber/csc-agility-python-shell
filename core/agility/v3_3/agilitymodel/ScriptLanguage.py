from core.agility.v3_3.agilitymodel.base.ScriptLanguage import ScriptLanguageBase
from core.agility.v3_3.agilitymodel.actions.ScriptLanguage import ScriptLanguageActions

class ScriptLanguage(ScriptLanguageBase, ScriptLanguageActions):
    '''
    classdocs
    '''
    def __init__(self, editormode=None, domain=None, operatingsystem=[], variableregex=None, interpreter=None, type=None):
        '''
        Constructor
        @param editormode: editormode minOccurs=0
        @type editormode: string
        @param domain: domain minOccurs=0
        @type domain: Link
        @param operatingsystem: operatingsystem minOccurs=0 maxOccurs=unbounded
        @type operatingsystem: string
        @param variableregex: variableregex minOccurs=0
        @type variableregex: string
        @param interpreter: interpreter minOccurs=0
        @type interpreter: string
        @param type: type minOccurs=0
        @type type: ScriptType
        '''
        ScriptLanguageBase.__init__(self, editormode=editormode, domain=domain, operatingsystem=operatingsystem, variableregex=variableregex, interpreter=interpreter, type=type)
