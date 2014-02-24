from VersionedItem import VersionedItemBase

class PackageBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, shutdown=list(), metaVariable=list(), startup=list(), operational=list(), dependency=list(), install=list(), reconfigure=list(), variable=list(), operatingSystem=list()):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'shutdown': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'shutdown', 'minOccurs': '0', 'native': False}, 'metaVariable': {'maxOccurs': 'unbounded', 'type': 'ScriptPropertyReference', 'name': 'metaVariable', 'minOccurs': '0', 'native': False}, 'startup': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'startup', 'minOccurs': '0', 'native': False}, 'operational': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'operational', 'minOccurs': '0', 'native': False}, 'reconfigure': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'reconfigure', 'minOccurs': '0', 'native': False}, 'dependency': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'dependency', 'minOccurs': '0', 'native': False}, 'install': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'install', 'minOccurs': '0', 'native': False}, 'variable': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'operatingSystem', 'minOccurs': '0', 'native': True}})
        self.shutdown = shutdown
        self.metaVariable = metaVariable
        self.startup = startup
        self.operational = operational
        self.dependency = dependency
        self.install = install
        self.reconfigure = reconfigure
        self.variable = variable
        self.operatingSystem = operatingSystem 
