from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class AttachmentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, content=None, attachmentlocation=[], size=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'content': {'native': True, 'name': 'content', 'minOccurs': '0', 'type': 'base64Binary'}, 'attachmentLocation': {'maxOccurs': 'unbounded', 'native': False, 'name': 'attachmentlocation', 'minOccurs': '0', 'type': 'AttachmentLocation'}, 'size': {'native': True, 'name': 'size', 'minOccurs': '0', 'type': 'long'}})
        self.content = content
        self.attachmentlocation = attachmentlocation
        self.size = size 
