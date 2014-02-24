from VersionedItem import VersionedItemBase

class StackBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, images=list(), baseStack=None, operatingSystem=None, template=None, targets=list()):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'images': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'images', 'minOccurs': '0', 'native': False}, 'baseStack': {'type': 'Link', 'name': 'baseStack', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'type': 'string', 'name': 'operatingSystem', 'minOccurs': '0', 'native': True}, 'template': {'type': 'Link', 'name': 'template', 'minOccurs': '0', 'native': False}, 'targets': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'targets', 'minOccurs': '0', 'native': False}})
        self.images = images
        self.baseStack = baseStack
        self.operatingSystem = operatingSystem
        self.template = template
        self.targets = targets 
