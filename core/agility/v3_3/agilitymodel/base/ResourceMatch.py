from core.agility.v3_3.agilitymodel.base.DescriptiveLink import DescriptiveLinkBase

class ResourceMatchBase(DescriptiveLinkBase):
    '''
    classdocs
    '''
    def __init__(self, rank=None, stackdefault=False, metric=[]):
        DescriptiveLinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'rank': {'name': 'rank', 'native': True, 'type': 'double'}, 'stackDefault': {'name': 'stackdefault', 'native': True, 'type': 'boolean'}, 'metric': {'name': 'metric', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ResourceMetric'}})
        self.rank = rank
        self.stackdefault = stackdefault
        self.metric = metric 
