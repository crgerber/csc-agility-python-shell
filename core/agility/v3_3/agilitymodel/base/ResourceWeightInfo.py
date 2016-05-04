from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceWeightInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, metricdisplayname='', metricname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metricDisplayName': {'type': 'string', 'name': 'metricdisplayname', 'native': True}, 'metricName': {'type': 'string', 'name': 'metricname', 'native': True}})
        self.metricdisplayname = metricdisplayname
        self.metricname = metricname 
