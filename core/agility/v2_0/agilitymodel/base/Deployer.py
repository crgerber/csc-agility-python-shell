from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class DeployerBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, deployScript=None, templates=list(), startScript=None, urlPrefix=None, stopScript=None, undeployScript=None, artifactType=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployScript': {'type': 'Link', 'name': 'deployScript', 'minOccurs': '0', 'native': False}, 'templates': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'templates', 'minOccurs': '0', 'native': False}, 'startScript': {'type': 'Link', 'name': 'startScript', 'minOccurs': '0', 'native': False}, 'urlPrefix': {'type': 'string', 'name': 'urlPrefix', 'minOccurs': '0', 'native': True}, 'stopScript': {'type': 'Link', 'name': 'stopScript', 'minOccurs': '0', 'native': False}, 'undeployScript': {'type': 'Link', 'name': 'undeployScript', 'minOccurs': '0', 'native': False}, 'artifactType': {'type': 'Link', 'name': 'artifactType', 'minOccurs': '0', 'native': False}})
        self.deployScript = deployScript
        self.templates = templates
        self.startScript = startScript
        self.urlPrefix = urlPrefix
        self.stopScript = stopScript
        self.undeployScript = undeployScript
        self.artifactType = artifactType 
