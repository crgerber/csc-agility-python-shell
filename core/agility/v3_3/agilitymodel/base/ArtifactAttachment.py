from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ArtifactAttachmentBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, content=None, artifact=None, size=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'content': {'native': True, 'name': 'content', 'minOccurs': '0', 'type': 'base64Binary'}, 'artifact': {'native': False, 'name': 'artifact', 'minOccurs': '0', 'type': 'Link'}, 'size': {'native': True, 'name': 'size', 'minOccurs': '0', 'type': 'long'}})
        self.content = content
        self.artifact = artifact
        self.size = size 
