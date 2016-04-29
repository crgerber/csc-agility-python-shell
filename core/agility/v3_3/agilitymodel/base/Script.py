from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class ScriptBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, delay=None, variable=[], language=None, erroraction=None, runasadmin=None, enableextensions=None, type=None, runonprovisiononly=None, operatingsystem=[], rebootrequired=None, attachments=[], retries=None, body=None, metavariable=[], timeout=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'delay': {'native': True, 'name': 'delay', 'minOccurs': '0', 'type': 'int'}, 'variable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variable', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'language': {'native': False, 'name': 'language', 'minOccurs': '0', 'type': 'Link'}, 'rebootRequired': {'native': True, 'name': 'rebootrequired', 'minOccurs': '0', 'type': 'boolean'}, 'runAsAdmin': {'native': True, 'name': 'runasadmin', 'minOccurs': '0', 'type': 'boolean'}, 'enableExtensions': {'native': True, 'name': 'enableextensions', 'minOccurs': '0', 'type': 'boolean'}, 'type': {'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'ScriptType'}, 'runOnProvisionOnly': {'native': True, 'name': 'runonprovisiononly', 'minOccurs': '0', 'type': 'boolean'}, 'attachments': {'maxOccurs': 'unbounded', 'native': False, 'name': 'attachments', 'minOccurs': '0', 'type': 'Link'}, 'retries': {'native': True, 'name': 'retries', 'minOccurs': '0', 'type': 'int'}, 'body': {'native': True, 'name': 'body', 'minOccurs': '0', 'type': 'string'}, 'operatingSystem': {'maxOccurs': 'unbounded', 'native': True, 'name': 'operatingsystem', 'minOccurs': '0', 'type': 'string'}, 'metaVariable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'metavariable', 'minOccurs': '0', 'type': 'ScriptPropertyReference'}, 'errorAction': {'native': False, 'name': 'erroraction', 'minOccurs': '0', 'type': 'ScriptErrorAction'}, 'timeout': {'native': True, 'name': 'timeout', 'minOccurs': '0', 'type': 'int'}})
        self.delay = delay
        self.variable = variable
        self.language = language
        self.erroraction = erroraction
        self.runasadmin = runasadmin
        self.enableextensions = enableextensions
        self.type = type
        self.runonprovisiononly = runonprovisiononly
        self.operatingsystem = operatingsystem
        self.rebootrequired = rebootrequired
        self.attachments = attachments
        self.retries = retries
        self.body = body
        self.metavariable = metavariable
        self.timeout = timeout 
