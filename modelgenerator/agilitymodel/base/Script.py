from VersionedItem import VersionedItemBase

class ScriptBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, body=None, retries=None, metaVariable=list(), attachments=list(), language=None, enableExtensions=None, runAsAdmin=None, delay=None, timeout=None, variable=list(), rebootRequired=None, type=None, operatingSystem=list(), errorAction=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'body': {'type': 'string', 'name': 'body', 'minOccurs': '0', 'native': True}, 'retries': {'type': 'int', 'name': 'retries', 'minOccurs': '0', 'native': True}, 'enableExtensions': {'type': 'boolean', 'name': 'enableExtensions', 'minOccurs': '0', 'native': True}, 'attachments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'attachments', 'minOccurs': '0', 'native': False}, 'language': {'type': 'Link', 'name': 'language', 'minOccurs': '0', 'native': False}, 'metaVariable': {'maxOccurs': 'unbounded', 'type': 'ScriptPropertyReference', 'name': 'metaVariable', 'minOccurs': '0', 'native': False}, 'runAsAdmin': {'type': 'boolean', 'name': 'runAsAdmin', 'minOccurs': '0', 'native': True}, 'delay': {'type': 'int', 'name': 'delay', 'minOccurs': '0', 'native': True}, 'timeout': {'type': 'int', 'name': 'timeout', 'minOccurs': '0', 'native': True}, 'variable': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'rebootRequired': {'type': 'boolean', 'name': 'rebootRequired', 'minOccurs': '0', 'native': True}, 'type': {'type': 'ScriptType', 'name': 'type', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'operatingSystem', 'minOccurs': '0', 'native': True}, 'errorAction': {'type': 'ScriptErrorAction', 'name': 'errorAction', 'minOccurs': '0', 'native': False}})
        self.body = body
        self.retries = retries
        self.metaVariable = metaVariable
        self.attachments = attachments
        self.language = language
        self.enableExtensions = enableExtensions
        self.runAsAdmin = runAsAdmin
        self.delay = delay
        self.timeout = timeout
        self.variable = variable
        self.rebootRequired = rebootRequired
        self.type = type
        self.operatingSystem = operatingSystem
        self.errorAction = errorAction 
