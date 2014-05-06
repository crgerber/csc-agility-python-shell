from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class AliasBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, link=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'link': {'type': 'Link', 'name': 'link', 'minOccurs': '0', 'native': False}})
        self.link = link 
