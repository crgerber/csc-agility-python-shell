from core.agility.v3_3.agilitymodel.base.ResourceMetric import ResourceMetricBase
from core.agility.v3_3.agilitymodel.actions.ResourceMetric import ResourceMetricActions

class ResourceMetric(ResourceMetricBase, ResourceMetricActions):
    '''
    classdocs
    '''
    def __init__(self, quantity=None, capacity=None, type=''):
        '''
        Constructor
        @param quantity: quantity
        @type quantity: double
        @param capacity: capacity
        @type capacity: double
        @param type: type
        @type type: string
        '''
        ResourceMetricBase.__init__(self, quantity=quantity, capacity=capacity, type=type)
