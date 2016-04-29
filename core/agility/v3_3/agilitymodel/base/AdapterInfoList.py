from core.agility.common.AgilityModelBase import AgilityModelBase

class AdapterInfoListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, adapterinfo=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'adapterInfo': {'maxOccurs': 'unbounded', 'native': False, 'name': 'adapterinfo', 'minOccurs': '0', 'type': 'AdapterInfo'}})
        self.adapterinfo = adapterinfo 
