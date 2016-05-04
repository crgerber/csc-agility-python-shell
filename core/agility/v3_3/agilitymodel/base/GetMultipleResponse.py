from core.agility.common.AgilityModelBase import AgilityModelBase

class GetMultipleResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, asset=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'asset': {'maxOccurs': 'unbounded', 'type': 'Asset', 'name': 'asset', 'minOccurs': '0', 'native': False}})
        self.asset = asset 
