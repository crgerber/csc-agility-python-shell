from .AgilityModelBase import AgilityModelBase

class LinklistBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, link=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'link': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'link', 'minOccurs': '0', 'native': False}})
        self.link = link 
