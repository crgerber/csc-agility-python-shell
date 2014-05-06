from AgilityModelBase import AgilityModelBase

class CustomItemListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, customitem=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customItem': {'maxOccurs': 'unbounded', 'type': 'CustomItem', 'name': 'customitem', 'minOccurs': '0', 'native': False}})
        self.customitem = customitem 
