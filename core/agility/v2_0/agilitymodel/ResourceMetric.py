from core.agility.v2_0.agilitymodel.base.ResourceMetric import ResourceMetricBase
from core.agility.v2_0.agilitymodel.actions.ResourceMetric import ResourceMetricActions

class ResourceMetric(ResourceMetricBase, ResourceMetricActions):
    '''
    classdocs
    '''
    def __init__(self, capacity=None, type='', quantity=None):
        '''
        Constructor
        @param capacity: capacity
        @type capacity: double
        @param type: type
        @type type: string
        @param quantity: quantity
        @type quantity: double
        '''
        ResourceMetricBase.__init__(self, capacity=capacity, type=type, quantity=quantity)
