from core.restclient.v2_0.agilitymodel.base.Link import LinkBase

class ResourceMatchBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, metric=list(), rank=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metric': {'maxOccurs': 'unbounded', 'type': 'ResourceMetric', 'name': 'metric', 'minOccurs': '0', 'native': False}, 'rank': {'type': 'double', 'name': 'rank', 'native': True}})
        self.metric = metric
        self.rank = rank 
