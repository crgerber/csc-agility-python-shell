from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class ResourceWeightBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, metric='', value=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metric': {'use': 'required', 'type': 'string', 'name': 'metric', 'native': True}, 'value': {'use': 'required', 'type': 'double', 'name': 'value', 'native': True}})
        self.metric = metric
        self.value = value 
