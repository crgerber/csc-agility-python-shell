from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class AccessUriListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, AccessUri=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'AccessUri': {'maxOccurs': 'unbounded', 'type': 'AccessUri', 'name': 'AccessUri', 'minOccurs': '0', 'native': False}})
        self.AccessUri = AccessUri 
