from core.agility.common.AgilityModelBase import AgilityModelBase


class AuthenticationListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, authentications=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'authentications': {'maxOccurs': 'unbounded', 'type': 'Authentication', 'name': 'authentications', 'minOccurs': '0', 'native': False}})
        self.authentications = authentications 
