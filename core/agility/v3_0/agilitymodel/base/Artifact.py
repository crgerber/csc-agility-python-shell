from core.agility.v3_0.agilitymodel.base.VersionedItem import VersionedItemBase

class ArtifactBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, buildid=None, configuration=None, builton=None, solution=None, attachments=[]):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'buildId': {'type': 'string', 'name': 'buildid', 'minOccurs': '0', 'native': True}, 'configuration': {'type': 'ArtifactConfiguration', 'name': 'configuration', 'minOccurs': '0', 'native': False}, 'builtOn': {'type': 'date', 'name': 'builton', 'minOccurs': '0', 'native': True}, 'solution': {'type': 'Link', 'name': 'solution', 'minOccurs': '0', 'native': False}, 'attachments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'attachments', 'minOccurs': '0', 'native': False}})
        self.buildid = buildid
        self.configuration = configuration
        self.builton = builton
        self.solution = solution
        self.attachments = attachments 
