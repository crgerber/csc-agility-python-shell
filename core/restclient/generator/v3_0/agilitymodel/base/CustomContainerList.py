from AgilityModelBase import AgilityModelBase

class CustomContainerListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, customcontainer=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customContainer': {'maxOccurs': 'unbounded', 'type': 'CustomContainer', 'name': 'customcontainer', 'minOccurs': '0', 'native': False}})
        self.customcontainer = customcontainer 
