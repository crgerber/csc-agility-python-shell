from Item import ItemBase

class DeployerBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, deployscript=None, templates=[], startscript=None, urlprefix=None, stopscript=None, undeployscript=None, artifacttype=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployScript': {'type': 'Link', 'name': 'deployscript', 'minOccurs': '0', 'native': False}, 'templates': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'templates', 'minOccurs': '0', 'native': False}, 'startScript': {'type': 'Link', 'name': 'startscript', 'minOccurs': '0', 'native': False}, 'urlPrefix': {'type': 'string', 'name': 'urlprefix', 'minOccurs': '0', 'native': True}, 'stopScript': {'type': 'Link', 'name': 'stopscript', 'minOccurs': '0', 'native': False}, 'undeployScript': {'type': 'Link', 'name': 'undeployscript', 'minOccurs': '0', 'native': False}, 'artifactType': {'type': 'Link', 'name': 'artifacttype', 'minOccurs': '0', 'native': False}})
        self.deployscript = deployscript
        self.templates = templates
        self.startscript = startscript
        self.urlprefix = urlprefix
        self.stopscript = stopscript
        self.undeployscript = undeployscript
        self.artifacttype = artifacttype 
