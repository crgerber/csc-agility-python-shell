from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ConfigurationRepositoryBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, repositorypath=None, artifact=[], repositorytype=None, readonly=False, repositoryproperty=[], artifacttype=None, artifactpath=[], syncintervalseconds=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'readOnly': {'name': 'readonly', 'native': True, 'type': 'boolean'}, 'artifact': {'name': 'artifact', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'repositoryType': {'name': 'repositorytype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'repositoryPath': {'name': 'repositorypath', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'repositoryProperty': {'name': 'repositoryproperty', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'artifactType': {'name': 'artifacttype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'artifactPath': {'name': 'artifactpath', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'syncIntervalSeconds': {'name': 'syncintervalseconds', 'minOccurs': '0', 'native': True, 'type': 'int'}})
        self.repositorypath = repositorypath
        self.artifact = artifact
        self.repositorytype = repositorytype
        self.readonly = readonly
        self.repositoryproperty = repositoryproperty
        self.artifacttype = artifacttype
        self.artifactpath = artifactpath
        self.syncintervalseconds = syncintervalseconds 
