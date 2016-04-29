from core.agility.v3_3.agilitymodel.base.ResourceWeightInfo import ResourceWeightInfoBase
from core.agility.v3_3.agilitymodel.actions.ResourceWeightInfo import ResourceWeightInfoActions

class ResourceWeightInfo(ResourceWeightInfoBase, ResourceWeightInfoActions):
    '''
    classdocs
    '''
    def __init__(self, metricname='', metricdisplayname=''):
        '''
        Constructor
        @param metricname: metricname
        @type metricname: string
        @param metricdisplayname: metricdisplayname
        @type metricdisplayname: string
        '''
        ResourceWeightInfoBase.__init__(self, metricname=metricname, metricdisplayname=metricdisplayname)
