from base.Script import ScriptBase
from actions.Script import ScriptActions

class Script(ScriptBase, ScriptActions):
    '''
    classdocs
    '''
    def __init__(self, body=None, retries=None, metavariable=[], attachments=[], language=None, runonprovisiononly=None, enableextensions=None, runasadmin=None, delay=None, timeout=None, variable=[], rebootrequired=None, type=None, operatingsystem=[], erroraction=None):
        '''
        Constructor
        @param body: body minOccurs=0
        @type body: string
        @param retries: retries minOccurs=0
        @type retries: int
        @param metavariable: metavariable minOccurs=0 maxOccurs=unbounded
        @type metavariable: ScriptPropertyReference
        @param attachments: attachments minOccurs=0 maxOccurs=unbounded
        @type attachments: Link
        @param language: language minOccurs=0
        @type language: Link
        @param runonprovisiononly: runonprovisiononly minOccurs=0
        @type runonprovisiononly: boolean
        @param enableextensions: enableextensions minOccurs=0
        @type enableextensions: boolean
        @param runasadmin: runasadmin minOccurs=0
        @type runasadmin: boolean
        @param delay: delay minOccurs=0
        @type delay: int
        @param timeout: timeout minOccurs=0
        @type timeout: int
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: PropertyDefinition
        @param rebootrequired: rebootrequired minOccurs=0
        @type rebootrequired: boolean
        @param type: type minOccurs=0
        @type type: ScriptType
        @param operatingsystem: operatingsystem minOccurs=0 maxOccurs=unbounded
        @type operatingsystem: string
        @param erroraction: erroraction minOccurs=0
        @type erroraction: ScriptErrorAction
        '''
        ScriptBase.__init__(self, body=body, retries=retries, metavariable=metavariable, attachments=attachments, language=language, runonprovisiononly=runonprovisiononly, enableextensions=enableextensions, runasadmin=runasadmin, delay=delay, timeout=timeout, variable=variable, rebootrequired=rebootrequired, type=type, operatingsystem=operatingsystem, erroraction=erroraction)
