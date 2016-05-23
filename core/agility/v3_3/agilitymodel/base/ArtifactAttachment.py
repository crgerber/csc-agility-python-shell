from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ArtifactAttachmentBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, size=None, content=None, artifact=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'size': {'name': 'size', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'content': {'name': 'content', 'minOccurs': '0', 'native': True, 'type': 'base64Binary'}, 'artifact': {'name': 'artifact', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.size = size
        self.content = content
        self.artifact = artifact 
