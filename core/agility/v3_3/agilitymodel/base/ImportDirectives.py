from core.agility.common.AgilityModelBase import AgilityModelBase

class ImportDirectivesBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, onnotfound=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'onNotFound': {'native': False, 'name': 'onnotfound', 'type': 'LookupFailCode'}})
        self.onnotfound = onnotfound 