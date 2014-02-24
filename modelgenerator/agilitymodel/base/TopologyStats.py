from AgilityModelBase import AgilityModelBase

class TopologyStatsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, numStarting=None, maxCount=None, numInstances=None, numDestroyed=None, numStopped=None, topologyId=None, numStopping=None, numFailed=None, numRunning=None, numUnknown=None, numTemplates=None, numDegraded=None, minCount=None, numPaused=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'numDegraded': {'type': 'int', 'name': 'numDegraded', 'native': True}, 'numInstances': {'type': 'int', 'name': 'numInstances', 'native': True}, 'numDestroyed': {'type': 'int', 'name': 'numDestroyed', 'native': True}, 'numStopped': {'type': 'int', 'name': 'numStopped', 'native': True}, 'topologyId': {'type': 'int', 'name': 'topologyId', 'native': True}, 'numStopping': {'type': 'int', 'name': 'numStopping', 'native': True}, 'numPaused': {'type': 'int', 'name': 'numPaused', 'native': True}, 'numFailed': {'type': 'int', 'name': 'numFailed', 'native': True}, 'numStarting': {'type': 'int', 'name': 'numStarting', 'native': True}, 'numUnknown': {'type': 'int', 'name': 'numUnknown', 'native': True}, 'numTemplates': {'type': 'int', 'name': 'numTemplates', 'native': True}, 'maxCount': {'type': 'int', 'name': 'maxCount', 'native': True}, 'minCount': {'type': 'int', 'name': 'minCount', 'native': True}, 'numRunning': {'type': 'int', 'name': 'numRunning', 'native': True}})
        self.numStarting = numStarting
        self.maxCount = maxCount
        self.numInstances = numInstances
        self.numDestroyed = numDestroyed
        self.numStopped = numStopped
        self.topologyId = topologyId
        self.numStopping = numStopping
        self.numFailed = numFailed
        self.numRunning = numRunning
        self.numUnknown = numUnknown
        self.numTemplates = numTemplates
        self.numDegraded = numDegraded
        self.minCount = minCount
        self.numPaused = numPaused 
