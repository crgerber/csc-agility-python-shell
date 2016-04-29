from core.agility.common.AgilityModelBase import AgilityModelBase

class GetMultipleResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, asset=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'asset': {'maxOccurs': 'unbounded', 'native': False, 'name': 'asset', 'minOccurs': '0', 'type': 'Asset'}})
        self.asset = asset 
