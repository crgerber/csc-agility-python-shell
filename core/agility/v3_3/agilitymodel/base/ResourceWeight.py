from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceWeightBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, value=None, metric=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'value': {'name': 'value', 'native': True, 'type': 'double', 'use': 'required'}, 'metric': {'name': 'metric', 'native': True, 'type': 'string', 'use': 'required'}})
        self.value = value
        self.metric = metric 
