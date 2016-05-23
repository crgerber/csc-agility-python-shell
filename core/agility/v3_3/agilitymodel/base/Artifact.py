from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class ArtifactBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, configuration=None, builton=None, buildid=None, attachments=[], solution=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'configuration': {'name': 'configuration', 'minOccurs': '0', 'native': False, 'type': 'ArtifactConfiguration'}, 'builtOn': {'name': 'builton', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'buildId': {'name': 'buildid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'solution': {'name': 'solution', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'attachments': {'name': 'attachments', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.configuration = configuration
        self.builton = builton
        self.buildid = buildid
        self.attachments = attachments
        self.solution = solution 
