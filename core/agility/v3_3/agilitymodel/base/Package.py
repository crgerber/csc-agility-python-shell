from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class PackageBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, operatingsystem=[], startup=[], shutdown=[], metavariable=[], variable=[], dependency=[], install=[], operational=[], reconfigure=[]):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'operatingSystem': {'name': 'operatingsystem', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'startup': {'name': 'startup', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'shutdown': {'name': 'shutdown', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'metaVariable': {'name': 'metavariable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ScriptPropertyReference'}, 'variable': {'name': 'variable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'dependency': {'name': 'dependency', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'install': {'name': 'install', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'operational': {'name': 'operational', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'reconfigure': {'name': 'reconfigure', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.operatingsystem = operatingsystem
        self.startup = startup
        self.shutdown = shutdown
        self.metavariable = metavariable
        self.variable = variable
        self.dependency = dependency
        self.install = install
        self.operational = operational
        self.reconfigure = reconfigure 
