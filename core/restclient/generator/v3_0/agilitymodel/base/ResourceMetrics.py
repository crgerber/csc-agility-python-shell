from AgilityModelBase import AgilityModelBase

class ResourceMetricsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, metric=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metric': {'maxOccurs': 'unbounded', 'type': 'ResourceMetric', 'name': 'metric', 'minOccurs': '0', 'native': False}})
        self.metric = metric 
