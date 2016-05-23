from core.agility.v3_3.agilitymodel.base.Script import ScriptBase
from core.agility.v3_3.agilitymodel.actions.Script import ScriptActions

class Script(ScriptBase, ScriptActions):
    '''
    classdocs
    '''
    def __init__(self, runasadmin=None, operatingsystem=[], timeout=None, metavariable=[], variable=[], body=None, runonprovisiononly=None, attachments=[], delay=None, language=None, rebootrequired=None, enableextensions=None, erroraction=None, type=None, retries=None):
        '''
        Constructor
        @param runasadmin: runasadmin minOccurs=0
        @type runasadmin: boolean
        @param operatingsystem: operatingsystem minOccurs=0 maxOccurs=unbounded
        @type operatingsystem: string
        @param timeout: timeout minOccurs=0
        @type timeout: int
        @param metavariable: metavariable minOccurs=0 maxOccurs=unbounded
        @type metavariable: ScriptPropertyReference
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: PropertyDefinition
        @param body: body minOccurs=0
        @type body: string
        @param runonprovisiononly: runonprovisiononly minOccurs=0
        @type runonprovisiononly: boolean
        @param attachments: attachments minOccurs=0 maxOccurs=unbounded
        @type attachments: Link
        @param delay: delay minOccurs=0
        @type delay: int
        @param language: language minOccurs=0
        @type language: Link
        @param rebootrequired: rebootrequired minOccurs=0
        @type rebootrequired: boolean
        @param enableextensions: enableextensions minOccurs=0
        @type enableextensions: boolean
        @param erroraction: erroraction minOccurs=0
        @type erroraction: ScriptErrorAction
        @param type: type minOccurs=0
        @type type: ScriptType
        @param retries: retries minOccurs=0
        @type retries: int
        '''
        ScriptBase.__init__(self, runasadmin=runasadmin, operatingsystem=operatingsystem, timeout=timeout, metavariable=metavariable, variable=variable, body=body, runonprovisiononly=runonprovisiononly, attachments=attachments, delay=delay, language=language, rebootrequired=rebootrequired, enableextensions=enableextensions, erroraction=erroraction, type=type, retries=retries)
