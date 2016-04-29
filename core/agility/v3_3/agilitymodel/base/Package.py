from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class PackageBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, startup=[], reconfigure=[], operational=[], dependency=[], shutdown=[], operatingsystem=[], metavariable=[], install=[], variable=[]):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'startup': {'maxOccurs': 'unbounded', 'native': False, 'name': 'startup', 'minOccurs': '0', 'type': 'Link'}, 'reconfigure': {'maxOccurs': 'unbounded', 'native': False, 'name': 'reconfigure', 'minOccurs': '0', 'type': 'Link'}, 'operational': {'maxOccurs': 'unbounded', 'native': False, 'name': 'operational', 'minOccurs': '0', 'type': 'Link'}, 'variable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variable', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'shutdown': {'maxOccurs': 'unbounded', 'native': False, 'name': 'shutdown', 'minOccurs': '0', 'type': 'Link'}, 'operatingSystem': {'maxOccurs': 'unbounded', 'native': True, 'name': 'operatingsystem', 'minOccurs': '0', 'type': 'string'}, 'dependency': {'maxOccurs': 'unbounded', 'native': False, 'name': 'dependency', 'minOccurs': '0', 'type': 'Link'}, 'install': {'maxOccurs': 'unbounded', 'native': False, 'name': 'install', 'minOccurs': '0', 'type': 'Link'}, 'metaVariable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'metavariable', 'minOccurs': '0', 'type': 'ScriptPropertyReference'}})
        self.startup = startup
        self.reconfigure = reconfigure
        self.operational = operational
        self.dependency = dependency
        self.shutdown = shutdown
        self.operatingsystem = operatingsystem
        self.metavariable = metavariable
        self.install = install
        self.variable = variable 
