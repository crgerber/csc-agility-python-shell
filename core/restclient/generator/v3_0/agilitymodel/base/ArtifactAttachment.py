from Item import ItemBase

class ArtifactAttachmentBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, content=None, artifact=None, size=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'content': {'type': 'base64Binary', 'name': 'content', 'minOccurs': '0', 'native': True}, 'artifact': {'type': 'Link', 'name': 'artifact', 'minOccurs': '0', 'native': False}, 'size': {'type': 'long', 'name': 'size', 'minOccurs': '0', 'native': True}})
        self.content = content
        self.artifact = artifact
        self.size = size 
