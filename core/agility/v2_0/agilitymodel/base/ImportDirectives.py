from core.agility.common.AgilityModelBase import AgilityModelBase


class ImportDirectivesBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, onNotFound=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'onNotFound': {'type': 'LookupFailCode', 'name': 'onNotFound', 'native': False}})
        self.onNotFound = onNotFound 
