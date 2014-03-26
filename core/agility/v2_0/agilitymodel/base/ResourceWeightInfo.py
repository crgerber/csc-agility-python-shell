from core.agility.common.AgilityModelBase import AgilityModelBase


class ResourceWeightInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, metricDisplayName='', metricName=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'metricDisplayName': {'type': 'string', 'name': 'metricDisplayName', 'native': True}, 'metricName': {'type': 'string', 'name': 'metricName', 'native': True}})
        self.metricDisplayName = metricDisplayName
        self.metricName = metricName 
