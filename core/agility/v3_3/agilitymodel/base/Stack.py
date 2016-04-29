from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class StackBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, template=None, basestack=None, operatingsystem=None, targets=[], status=None, images=[]):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'template': {'native': False, 'name': 'template', 'minOccurs': '0', 'type': 'Link'}, 'baseStack': {'native': False, 'name': 'basestack', 'minOccurs': '0', 'type': 'Link'}, 'operatingSystem': {'native': True, 'name': 'operatingsystem', 'minOccurs': '0', 'type': 'string'}, 'targets': {'maxOccurs': 'unbounded', 'native': False, 'name': 'targets', 'minOccurs': '0', 'type': 'Link'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'images': {'maxOccurs': 'unbounded', 'native': False, 'name': 'images', 'minOccurs': '0', 'type': 'Link'}})
        self.template = template
        self.basestack = basestack
        self.operatingsystem = operatingsystem
        self.targets = targets
        self.status = status
        self.images = images 
