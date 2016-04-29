from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceWeightInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, metricname='', metricdisplayname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metricName': {'native': True, 'name': 'metricname', 'type': 'string'}, 'metricDisplayName': {'native': True, 'name': 'metricdisplayname', 'type': 'string'}})
        self.metricname = metricname
        self.metricdisplayname = metricdisplayname 
