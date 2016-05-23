from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceMetricsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, metric=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metric': {'name': 'metric', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ResourceMetric'}})
        self.metric = metric 
