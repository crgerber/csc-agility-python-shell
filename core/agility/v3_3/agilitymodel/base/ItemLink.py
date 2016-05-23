from core.agility.v3_3.agilitymodel.base.Link import LinkBase

class ItemLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'parent': {'name': 'parent', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.parent = parent 
