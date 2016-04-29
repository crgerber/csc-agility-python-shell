from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class ArtifactBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, configuration=None, buildid=None, solution=None, attachments=[], builton=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'attachments': {'maxOccurs': 'unbounded', 'native': False, 'name': 'attachments', 'minOccurs': '0', 'type': 'Link'}, 'buildId': {'native': True, 'name': 'buildid', 'minOccurs': '0', 'type': 'string'}, 'solution': {'native': False, 'name': 'solution', 'minOccurs': '0', 'type': 'Link'}, 'configuration': {'native': False, 'name': 'configuration', 'minOccurs': '0', 'type': 'ArtifactConfiguration'}, 'builtOn': {'native': True, 'name': 'builton', 'minOccurs': '0', 'type': 'date'}})
        self.configuration = configuration
        self.buildid = buildid
        self.solution = solution
        self.attachments = attachments
        self.builton = builton 
