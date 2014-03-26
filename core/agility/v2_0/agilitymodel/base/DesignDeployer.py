from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class DesignDeployerBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, deployScript=None, startScript=None, designContainer=None, urlPrefix=None, stopScript=None, undeployScript=None, artifactType=None, workloads=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployScript': {'type': 'Link', 'name': 'deployScript', 'minOccurs': '0', 'native': False}, 'startScript': {'type': 'Link', 'name': 'startScript', 'minOccurs': '0', 'native': False}, 'designContainer': {'type': 'Link', 'name': 'designContainer', 'minOccurs': '0', 'native': False}, 'urlPrefix': {'type': 'string', 'name': 'urlPrefix', 'minOccurs': '0', 'native': True}, 'stopScript': {'type': 'Link', 'name': 'stopScript', 'minOccurs': '0', 'native': False}, 'undeployScript': {'type': 'Link', 'name': 'undeployScript', 'minOccurs': '0', 'native': False}, 'artifactType': {'type': 'Link', 'name': 'artifactType', 'minOccurs': '0', 'native': False}, 'workloads': {'maxOccurs': 'unbounded', 'type': 'LogicalLink', 'name': 'workloads', 'minOccurs': '0', 'native': False}})
        self.deployScript = deployScript
        self.startScript = startScript
        self.designContainer = designContainer
        self.urlPrefix = urlPrefix
        self.stopScript = stopScript
        self.undeployScript = undeployScript
        self.artifactType = artifactType
        self.workloads = workloads 
