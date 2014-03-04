from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class ImportDirectivesBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, onNotFound=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'onNotFound': {'type': 'LookupFailCode', 'name': 'onNotFound', 'native': False}})
        self.onNotFound = onNotFound 
