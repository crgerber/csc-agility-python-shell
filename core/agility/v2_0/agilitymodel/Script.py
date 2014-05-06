from core.agility.v2_0.agilitymodel.base.Script import ScriptBase
from core.agility.v2_0.agilitymodel.actions.Script import ScriptActions

class Script(ScriptBase, ScriptActions):
    '''
    classdocs
    '''
    def __init__(self, body=None, retries=None, metaVariable=list(), attachments=list(), language=None, enableExtensions=None, runAsAdmin=None, delay=None, timeout=None, variable=list(), rebootRequired=None, type=None, operatingSystem=list(), errorAction=None):
        '''
        Constructor
        @param body: body minOccurs=0
        @type body: string
        @param retries: retries minOccurs=0
        @type retries: int
        @param metaVariable: metaVariable minOccurs=0 maxOccurs=unbounded
        @type metaVariable: ScriptPropertyReference
        @param attachments: attachments minOccurs=0 maxOccurs=unbounded
        @type attachments: Link
        @param language: language minOccurs=0
        @type language: Link
        @param enableExtensions: enableExtensions minOccurs=0
        @type enableExtensions: boolean
        @param runAsAdmin: runAsAdmin minOccurs=0
        @type runAsAdmin: boolean
        @param delay: delay minOccurs=0
        @type delay: int
        @param timeout: timeout minOccurs=0
        @type timeout: int
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: PropertyDefinition
        @param rebootRequired: rebootRequired minOccurs=0
        @type rebootRequired: boolean
        @param type: type minOccurs=0
        @type type: ScriptType
        @param operatingSystem: operatingSystem minOccurs=0 maxOccurs=unbounded
        @type operatingSystem: string
        @param errorAction: errorAction minOccurs=0
        @type errorAction: ScriptErrorAction
        '''
        ScriptBase.__init__(self, body=body, retries=retries, metaVariable=metaVariable, attachments=attachments, language=language, enableExtensions=enableExtensions, runAsAdmin=runAsAdmin, delay=delay, timeout=timeout, variable=variable, rebootRequired=rebootRequired, type=type, operatingSystem=operatingSystem, errorAction=errorAction)
