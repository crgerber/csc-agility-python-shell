from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ConfigurationRepositoryBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, repositoryproperty=[], artifactpath=[], repositorytype=None, artifact=[], repositorypath=None, readonly=False, syncintervalseconds=None, artifacttype=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'repositoryProperty': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'repositoryproperty', 'minOccurs': '0', 'native': False}, 'artifactPath': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'artifactpath', 'minOccurs': '0', 'native': True}, 'repositoryType': {'type': 'string', 'name': 'repositorytype', 'minOccurs': '0', 'native': True}, 'artifact': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'artifact', 'minOccurs': '0', 'native': False}, 'repositoryPath': {'type': 'string', 'name': 'repositorypath', 'minOccurs': '0', 'native': True}, 'readOnly': {'type': 'boolean', 'name': 'readonly', 'native': True}, 'syncIntervalSeconds': {'type': 'int', 'name': 'syncintervalseconds', 'minOccurs': '0', 'native': True}, 'artifactType': {'type': 'string', 'name': 'artifacttype', 'minOccurs': '0', 'native': True}})
        self.repositoryproperty = repositoryproperty
        self.artifactpath = artifactpath
        self.repositorytype = repositorytype
        self.artifact = artifact
        self.repositorypath = repositorypath
        self.readonly = readonly
        self.syncintervalseconds = syncintervalseconds
        self.artifacttype = artifacttype 
