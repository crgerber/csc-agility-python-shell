from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class DesignDeployerBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, startscript=None, stopscript=None, undeployscript=None, workloads=[], artifacttype=None, deployscript=None, designcontainer=None, urlprefix=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'startScript': {'name': 'startscript', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'stopScript': {'name': 'stopscript', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'undeployScript': {'name': 'undeployscript', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'workloads': {'name': 'workloads', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'LogicalLink'}, 'artifactType': {'name': 'artifacttype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'deployScript': {'name': 'deployscript', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'designContainer': {'name': 'designcontainer', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'urlPrefix': {'name': 'urlprefix', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.startscript = startscript
        self.stopscript = stopscript
        self.undeployscript = undeployscript
        self.workloads = workloads
        self.artifacttype = artifacttype
        self.deployscript = deployscript
        self.designcontainer = designcontainer
        self.urlprefix = urlprefix 
