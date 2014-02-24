from base.TopologyStats import TopologyStatsBase
from actions.TopologyStats import TopologyStatsActions

class TopologyStats(TopologyStatsBase, TopologyStatsActions):
    '''
    classdocs
    '''
    def __init__(self, numStarting=None, maxCount=None, numInstances=None, numDestroyed=None, numStopped=None, topologyId=None, numStopping=None, numFailed=None, numRunning=None, numUnknown=None, numTemplates=None, numDegraded=None, minCount=None, numPaused=None):
        '''
        Constructor
        @param numStarting: numStarting
        @type numStarting: int
        @param maxCount: maxCount
        @type maxCount: int
        @param numInstances: numInstances
        @type numInstances: int
        @param numDestroyed: numDestroyed
        @type numDestroyed: int
        @param numStopped: numStopped
        @type numStopped: int
        @param topologyId: topologyId
        @type topologyId: int
        @param numStopping: numStopping
        @type numStopping: int
        @param numFailed: numFailed
        @type numFailed: int
        @param numRunning: numRunning
        @type numRunning: int
        @param numUnknown: numUnknown
        @type numUnknown: int
        @param numTemplates: numTemplates
        @type numTemplates: int
        @param numDegraded: numDegraded
        @type numDegraded: int
        @param minCount: minCount
        @type minCount: int
        @param numPaused: numPaused
        @type numPaused: int
        '''
        TopologyStatsBase.__init__(self, numStarting=numStarting, maxCount=maxCount, numInstances=numInstances, numDestroyed=numDestroyed, numStopped=numStopped, topologyId=topologyId, numStopping=numStopping, numFailed=numFailed, numRunning=numRunning, numUnknown=numUnknown, numTemplates=numTemplates, numDegraded=numDegraded, minCount=minCount, numPaused=numPaused)
