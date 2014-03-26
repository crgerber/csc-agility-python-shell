from core.agility.v3_0.agilitymodel.base.DescriptiveLink import DescriptiveLinkBase

class ResourceMatchBase(DescriptiveLinkBase):
    '''
    classdocs
    '''
    def __init__(self, metric=[], stackdefault=False, rank=None):
        DescriptiveLinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metric': {'maxOccurs': 'unbounded', 'type': 'ResourceMetric', 'name': 'metric', 'minOccurs': '0', 'native': False}, 'stackDefault': {'type': 'boolean', 'name': 'stackdefault', 'native': True}, 'rank': {'type': 'double', 'name': 'rank', 'native': True}})
        self.metric = metric
        self.stackdefault = stackdefault
        self.rank = rank 
