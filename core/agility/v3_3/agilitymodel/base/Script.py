from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class ScriptBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, runasadmin=None, operatingsystem=[], timeout=None, metavariable=[], variable=[], body=None, runonprovisiononly=None, attachments=[], delay=None, language=None, rebootrequired=None, enableextensions=None, erroraction=None, type=None, retries=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'retries': {'name': 'retries', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'runAsAdmin': {'name': 'runasadmin', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'errorAction': {'name': 'erroraction', 'minOccurs': '0', 'native': False, 'type': 'ScriptErrorAction'}, 'operatingSystem': {'name': 'operatingsystem', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'timeout': {'name': 'timeout', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'metaVariable': {'name': 'metavariable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ScriptPropertyReference'}, 'variable': {'name': 'variable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'body': {'name': 'body', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'runOnProvisionOnly': {'name': 'runonprovisiononly', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'delay': {'name': 'delay', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'language': {'name': 'language', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'enableExtensions': {'name': 'enableextensions', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'rebootRequired': {'name': 'rebootrequired', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': False, 'type': 'ScriptType'}, 'attachments': {'name': 'attachments', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.runasadmin = runasadmin
        self.operatingsystem = operatingsystem
        self.timeout = timeout
        self.metavariable = metavariable
        self.variable = variable
        self.body = body
        self.runonprovisiononly = runonprovisiononly
        self.attachments = attachments
        self.delay = delay
        self.language = language
        self.rebootrequired = rebootrequired
        self.enableextensions = enableextensions
        self.erroraction = erroraction
        self.type = type
        self.retries = retries 
