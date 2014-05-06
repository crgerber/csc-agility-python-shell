from Item import ItemBase

class DesignDeployerBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, deployscript=None, startscript=None, designcontainer=None, urlprefix=None, stopscript=None, undeployscript=None, artifacttype=None, workloads=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployScript': {'type': 'Link', 'name': 'deployscript', 'minOccurs': '0', 'native': False}, 'startScript': {'type': 'Link', 'name': 'startscript', 'minOccurs': '0', 'native': False}, 'designContainer': {'type': 'Link', 'name': 'designcontainer', 'minOccurs': '0', 'native': False}, 'urlPrefix': {'type': 'string', 'name': 'urlprefix', 'minOccurs': '0', 'native': True}, 'stopScript': {'type': 'Link', 'name': 'stopscript', 'minOccurs': '0', 'native': False}, 'undeployScript': {'type': 'Link', 'name': 'undeployscript', 'minOccurs': '0', 'native': False}, 'artifactType': {'type': 'Link', 'name': 'artifacttype', 'minOccurs': '0', 'native': False}, 'workloads': {'maxOccurs': 'unbounded', 'type': 'LogicalLink', 'name': 'workloads', 'minOccurs': '0', 'native': False}})
        self.deployscript = deployscript
        self.startscript = startscript
        self.designcontainer = designcontainer
        self.urlprefix = urlprefix
        self.stopscript = stopscript
        self.undeployscript = undeployscript
        self.artifacttype = artifacttype
        self.workloads = workloads 
