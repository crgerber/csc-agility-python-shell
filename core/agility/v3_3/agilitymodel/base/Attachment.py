from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class AttachmentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, size=None, content=None, attachmentlocation=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'size': {'name': 'size', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'content': {'name': 'content', 'minOccurs': '0', 'native': True, 'type': 'base64Binary'}, 'attachmentLocation': {'name': 'attachmentlocation', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AttachmentLocation'}})
        self.size = size
        self.content = content
        self.attachmentlocation = attachmentlocation 
