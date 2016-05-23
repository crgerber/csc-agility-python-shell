from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceWeightInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, metricdisplayname='', metricname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metricDisplayName': {'name': 'metricdisplayname', 'native': True, 'type': 'string'}, 'metricName': {'name': 'metricname', 'native': True, 'type': 'string'}})
        self.metricdisplayname = metricdisplayname
        self.metricname = metricname 
