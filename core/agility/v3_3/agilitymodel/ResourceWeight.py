from core.agility.v3_3.agilitymodel.base.ResourceWeight import ResourceWeightBase
from core.agility.v3_3.agilitymodel.actions.ResourceWeight import ResourceWeightActions

class ResourceWeight(ResourceWeightBase, ResourceWeightActions):
    '''
    classdocs
    '''
    def __init__(self, value=None, metric=''):
        '''
        Constructor
        @param value: value
        @type value: double
        @param metric: metric
        @type metric: string
        '''
        ResourceWeightBase.__init__(self, value=value, metric=metric)
