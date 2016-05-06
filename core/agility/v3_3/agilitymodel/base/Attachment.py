from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class AttachmentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, content=None, attachmentlocation=[], size=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'content': {'type': 'base64Binary', 'name': 'content', 'minOccurs': '0', 'native': True}, 'attachmentLocation': {'maxOccurs': 'unbounded', 'type': 'AttachmentLocation', 'name': 'attachmentlocation', 'minOccurs': '0', 'native': False}, 'size': {'type': 'long', 'name': 'size', 'minOccurs': '0', 'native': True}})
        self.content = content
        self.attachmentlocation = attachmentlocation
        self.size = size 
