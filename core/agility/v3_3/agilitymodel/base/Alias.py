from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AliasBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, link=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'link': {'native': False, 'name': 'link', 'minOccurs': '0', 'type': 'Link'}})
        self.link = link 