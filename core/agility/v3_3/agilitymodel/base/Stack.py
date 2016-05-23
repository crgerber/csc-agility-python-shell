from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class StackBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, operatingsystem=None, status=None, template=None, images=[], basestack=None, targets=[]):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'operatingSystem': {'name': 'operatingsystem', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'template': {'name': 'template', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'images': {'name': 'images', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'baseStack': {'name': 'basestack', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'targets': {'name': 'targets', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.operatingsystem = operatingsystem
        self.status = status
        self.template = template
        self.images = images
        self.basestack = basestack
        self.targets = targets 
