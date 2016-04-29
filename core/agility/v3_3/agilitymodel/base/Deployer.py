from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class DeployerBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, deployscript=None, templates=[], stopscript=None, artifacttype=None, startscript=None, undeployscript=None, urlprefix=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployScript': {'native': False, 'name': 'deployscript', 'minOccurs': '0', 'type': 'Link'}, 'templates': {'maxOccurs': 'unbounded', 'native': False, 'name': 'templates', 'minOccurs': '0', 'type': 'Link'}, 'stopScript': {'native': False, 'name': 'stopscript', 'minOccurs': '0', 'type': 'Link'}, 'artifactType': {'native': False, 'name': 'artifacttype', 'minOccurs': '0', 'type': 'Link'}, 'startScript': {'native': False, 'name': 'startscript', 'minOccurs': '0', 'type': 'Link'}, 'undeployScript': {'native': False, 'name': 'undeployscript', 'minOccurs': '0', 'type': 'Link'}, 'urlPrefix': {'native': True, 'name': 'urlprefix', 'minOccurs': '0', 'type': 'string'}})
        self.deployscript = deployscript
        self.templates = templates
        self.stopscript = stopscript
        self.artifacttype = artifacttype
        self.startscript = startscript
        self.undeployscript = undeployscript
        self.urlprefix = urlprefix 
