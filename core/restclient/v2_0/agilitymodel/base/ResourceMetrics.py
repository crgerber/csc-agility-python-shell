from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class ResourceMetricsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, metric=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metric': {'maxOccurs': 'unbounded', 'type': 'ResourceMetric', 'name': 'metric', 'minOccurs': '0', 'native': False}})
        self.metric = metric 
