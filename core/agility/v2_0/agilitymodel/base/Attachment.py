from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class AttachmentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, content=None, attachmentLocation=list(), size=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'content': {'type': 'base64Binary', 'name': 'content', 'minOccurs': '0', 'native': True}, 'attachmentLocation': {'maxOccurs': 'unbounded', 'type': 'AttachmentLocation', 'name': 'attachmentLocation', 'minOccurs': '0', 'native': False}, 'size': {'type': 'long', 'name': 'size', 'minOccurs': '0', 'native': True}})
        self.content = content
        self.attachmentLocation = attachmentLocation
        self.size = size 
