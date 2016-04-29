from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceWeightBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, metric='', value=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metric': {'native': True, 'name': 'metric', 'use': 'required', 'type': 'string'}, 'value': {'native': True, 'name': 'value', 'use': 'required', 'type': 'double'}})
        self.metric = metric
        self.value = value 
