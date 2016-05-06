from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class StackBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, targets=[], template=None, images=[], basestack=None, operatingsystem=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'operatingSystem': {'type': 'string', 'name': 'operatingsystem', 'minOccurs': '0', 'native': True}, 'template': {'type': 'Link', 'name': 'template', 'minOccurs': '0', 'native': False}, 'images': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'images', 'minOccurs': '0', 'native': False}, 'baseStack': {'type': 'Link', 'name': 'basestack', 'minOccurs': '0', 'native': False}, 'targets': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'targets', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.targets = targets
        self.template = template
        self.images = images
        self.basestack = basestack
        self.operatingsystem = operatingsystem 
