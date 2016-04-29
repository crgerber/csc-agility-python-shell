from core.agility.v3_3.agilitymodel.base.Script import ScriptBase
from core.agility.v3_3.agilitymodel.actions.Script import ScriptActions

class Script(ScriptBase, ScriptActions):
    '''
    classdocs
    '''
    def __init__(self, delay=None, variable=[], language=None, erroraction=None, runasadmin=None, enableextensions=None, type=None, runonprovisiononly=None, operatingsystem=[], rebootrequired=None, attachments=[], retries=None, body=None, metavariable=[], timeout=None):
        '''
        Constructor
        @param delay: delay minOccurs=0
        @type delay: int
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: PropertyDefinition
        @param language: language minOccurs=0
        @type language: Link
        @param erroraction: erroraction minOccurs=0
        @type erroraction: ScriptErrorAction
        @param runasadmin: runasadmin minOccurs=0
        @type runasadmin: boolean
        @param enableextensions: enableextensions minOccurs=0
        @type enableextensions: boolean
        @param type: type minOccurs=0
        @type type: ScriptType
        @param runonprovisiononly: runonprovisiononly minOccurs=0
        @type runonprovisiononly: boolean
        @param operatingsystem: operatingsystem minOccurs=0 maxOccurs=unbounded
        @type operatingsystem: string
        @param rebootrequired: rebootrequired minOccurs=0
        @type rebootrequired: boolean
        @param attachments: attachments minOccurs=0 maxOccurs=unbounded
        @type attachments: Link
        @param retries: retries minOccurs=0
        @type retries: int
        @param body: body minOccurs=0
        @type body: string
        @param metavariable: metavariable minOccurs=0 maxOccurs=unbounded
        @type metavariable: ScriptPropertyReference
        @param timeout: timeout minOccurs=0
        @type timeout: int
        '''
        ScriptBase.__init__(self, delay=delay, variable=variable, language=language, erroraction=erroraction, runasadmin=runasadmin, enableextensions=enableextensions, type=type, runonprovisiononly=runonprovisiononly, operatingsystem=operatingsystem, rebootrequired=rebootrequired, attachments=attachments, retries=retries, body=body, metavariable=metavariable, timeout=timeout)
