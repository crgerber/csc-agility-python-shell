from Item import ItemBase

class PlannerApplicationBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
