from core.agility.v2_0.agilitymodel.base.ResourceWeightInfo import ResourceWeightInfoBase
from core.agility.v2_0.agilitymodel.actions.ResourceWeightInfo import ResourceWeightInfoActions

class ResourceWeightInfo(ResourceWeightInfoBase, ResourceWeightInfoActions):
    '''
    classdocs
    '''
    def __init__(self, metricDisplayName='', metricName=''):
        '''
        Constructor
        @param metricDisplayName: metricDisplayName
        @type metricDisplayName: string
        @param metricName: metricName
        @type metricName: string
        '''
        ResourceWeightInfoBase.__init__(self, metricDisplayName=metricDisplayName, metricName=metricName)
