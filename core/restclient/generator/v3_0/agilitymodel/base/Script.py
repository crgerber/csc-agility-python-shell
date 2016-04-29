from .VersionedItem import VersionedItemBase

class ScriptBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, body=None, retries=None, metavariable=[], attachments=[], language=None, runonprovisiononly=None, enableextensions=None, runasadmin=None, delay=None, timeout=None, variable=[], rebootrequired=None, type=None, operatingsystem=[], erroraction=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'body': {'type': 'string', 'name': 'body', 'minOccurs': '0', 'native': True}, 'retries': {'type': 'int', 'name': 'retries', 'minOccurs': '0', 'native': True}, 'enableExtensions': {'type': 'boolean', 'name': 'enableextensions', 'minOccurs': '0', 'native': True}, 'attachments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'attachments', 'minOccurs': '0', 'native': False}, 'language': {'type': 'Link', 'name': 'language', 'minOccurs': '0', 'native': False}, 'runOnProvisionOnly': {'type': 'boolean', 'name': 'runonprovisiononly', 'minOccurs': '0', 'native': True}, 'metaVariable': {'maxOccurs': 'unbounded', 'type': 'ScriptPropertyReference', 'name': 'metavariable', 'minOccurs': '0', 'native': False}, 'runAsAdmin': {'type': 'boolean', 'name': 'runasadmin', 'minOccurs': '0', 'native': True}, 'delay': {'type': 'int', 'name': 'delay', 'minOccurs': '0', 'native': True}, 'timeout': {'type': 'int', 'name': 'timeout', 'minOccurs': '0', 'native': True}, 'variable': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'rebootRequired': {'type': 'boolean', 'name': 'rebootrequired', 'minOccurs': '0', 'native': True}, 'type': {'type': 'ScriptType', 'name': 'type', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'operatingsystem', 'minOccurs': '0', 'native': True}, 'errorAction': {'type': 'ScriptErrorAction', 'name': 'erroraction', 'minOccurs': '0', 'native': False}})
        self.body = body
        self.retries = retries
        self.metavariable = metavariable
        self.attachments = attachments
        self.language = language
        self.runonprovisiononly = runonprovisiononly
        self.enableextensions = enableextensions
        self.runasadmin = runasadmin
        self.delay = delay
        self.timeout = timeout
        self.variable = variable
        self.rebootrequired = rebootrequired
        self.type = type
        self.operatingsystem = operatingsystem
        self.erroraction = erroraction 
