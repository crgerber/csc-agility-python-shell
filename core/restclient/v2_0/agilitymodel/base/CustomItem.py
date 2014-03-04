from core.restclient.v2_0.agilitymodel.base.Item import ItemBase

class CustomItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
