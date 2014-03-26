from core.agility.common.AgilityModelBase import AgilityModelBase


class CustomContainerListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, customContainer=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customContainer': {'maxOccurs': 'unbounded', 'type': 'CustomContainer', 'name': 'customContainer', 'minOccurs': '0', 'native': False}})
        self.customContainer = customContainer 
