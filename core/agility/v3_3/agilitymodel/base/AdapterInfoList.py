from core.agility.common.AgilityModelBase import AgilityModelBase

class AdapterInfoListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, adapterinfo=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'adapterInfo': {'name': 'adapterinfo', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AdapterInfo'}})
        self.adapterinfo = adapterinfo 
