from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ConfigurationRepositoryBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, artifacttype=None, repositoryproperty=[], artifactpath=[], repositorytype=None, readonly=False, artifact=[], syncintervalseconds=None, repositorypath=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifactType': {'native': True, 'name': 'artifacttype', 'minOccurs': '0', 'type': 'string'}, 'repositoryProperty': {'maxOccurs': 'unbounded', 'native': False, 'name': 'repositoryproperty', 'minOccurs': '0', 'type': 'Property'}, 'artifactPath': {'maxOccurs': 'unbounded', 'native': True, 'name': 'artifactpath', 'minOccurs': '0', 'type': 'string'}, 'repositoryType': {'native': True, 'name': 'repositorytype', 'minOccurs': '0', 'type': 'string'}, 'readOnly': {'native': True, 'name': 'readonly', 'type': 'boolean'}, 'artifact': {'maxOccurs': 'unbounded', 'native': False, 'name': 'artifact', 'minOccurs': '0', 'type': 'Link'}, 'syncIntervalSeconds': {'native': True, 'name': 'syncintervalseconds', 'minOccurs': '0', 'type': 'int'}, 'repositoryPath': {'native': True, 'name': 'repositorypath', 'minOccurs': '0', 'type': 'string'}})
        self.artifacttype = artifacttype
        self.repositoryproperty = repositoryproperty
        self.artifactpath = artifactpath
        self.repositorytype = repositorytype
        self.readonly = readonly
        self.artifact = artifact
        self.syncintervalseconds = syncintervalseconds
        self.repositorypath = repositorypath 
