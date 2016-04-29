from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class GetMultipleRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, link=[]):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'link': {'maxOccurs': 'unbounded', 'native': False, 'name': 'link', 'minOccurs': '0', 'type': 'Link'}})
        self.link = link 
