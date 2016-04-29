from .base.ResourceWeightInfo import ResourceWeightInfoBase
from .actions.ResourceWeightInfo import ResourceWeightInfoActions

class ResourceWeightInfo(ResourceWeightInfoBase, ResourceWeightInfoActions):
    '''
    classdocs
    '''
    def __init__(self, metricdisplayname='', metricname=''):
        '''
        Constructor
        @param metricdisplayname: metricdisplayname
        @type metricdisplayname: string
        @param metricname: metricname
        @type metricname: string
        '''
        ResourceWeightInfoBase.__init__(self, metricdisplayname=metricdisplayname, metricname=metricname)
