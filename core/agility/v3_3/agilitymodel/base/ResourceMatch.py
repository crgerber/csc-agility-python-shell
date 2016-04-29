from core.agility.v3_3.agilitymodel.base.DescriptiveLink import DescriptiveLinkBase

class ResourceMatchBase(DescriptiveLinkBase):
    '''
    classdocs
    '''
    def __init__(self, metric=[], rank=None, stackdefault=False):
        DescriptiveLinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metric': {'maxOccurs': 'unbounded', 'native': False, 'name': 'metric', 'minOccurs': '0', 'type': 'ResourceMetric'}, 'rank': {'native': True, 'name': 'rank', 'type': 'double'}, 'stackDefault': {'native': True, 'name': 'stackdefault', 'type': 'boolean'}})
        self.metric = metric
        self.rank = rank
        self.stackdefault = stackdefault 
