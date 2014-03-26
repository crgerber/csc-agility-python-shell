from core.agility.v2_0.agilitymodel.base.VersionedItem import VersionedItemBase

class ArtifactBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, buildId=None, configuration=None, builtOn=None, solution=None, attachments=list()):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'buildId': {'type': 'string', 'name': 'buildId', 'minOccurs': '0', 'native': True}, 'configuration': {'type': 'ArtifactConfiguration', 'name': 'configuration', 'minOccurs': '0', 'native': False}, 'builtOn': {'type': 'date', 'name': 'builtOn', 'minOccurs': '0', 'native': True}, 'solution': {'type': 'Link', 'name': 'solution', 'minOccurs': '0', 'native': False}, 'attachments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'attachments', 'minOccurs': '0', 'native': False}})
        self.buildId = buildId
        self.configuration = configuration
        self.builtOn = builtOn
        self.solution = solution
        self.attachments = attachments 
