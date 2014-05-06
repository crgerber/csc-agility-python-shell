from core.agility.v2_0.agilitymodel.base.ResourceWeight import ResourceWeightBase
from core.agility.v2_0.agilitymodel.actions.ResourceWeight import ResourceWeightActions

class ResourceWeight(ResourceWeightBase, ResourceWeightActions):
    '''
    classdocs
    '''
    def __init__(self, metric='', value=None):
        '''
        Constructor
        @param metric: metric
        @type metric: string
        @param value: value
        @type value: double
        '''
        ResourceWeightBase.__init__(self, metric=metric, value=value)
