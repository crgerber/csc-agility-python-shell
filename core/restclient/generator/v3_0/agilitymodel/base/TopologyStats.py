from .AgilityModelBase import AgilityModelBase

class TopologyStatsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, numstarting=None, maxcount=None, numinstances=None, numdestroyed=None, numstopped=None, topologyid=None, numstopping=None, numfailed=None, numrunning=None, numunknown=None, numtemplates=None, numdegraded=None, mincount=None, numpaused=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'numDegraded': {'type': 'int', 'name': 'numdegraded', 'native': True}, 'numInstances': {'type': 'int', 'name': 'numinstances', 'native': True}, 'numDestroyed': {'type': 'int', 'name': 'numdestroyed', 'native': True}, 'numStopped': {'type': 'int', 'name': 'numstopped', 'native': True}, 'topologyId': {'type': 'int', 'name': 'topologyid', 'native': True}, 'numStopping': {'type': 'int', 'name': 'numstopping', 'native': True}, 'numPaused': {'type': 'int', 'name': 'numpaused', 'native': True}, 'numFailed': {'type': 'int', 'name': 'numfailed', 'native': True}, 'numStarting': {'type': 'int', 'name': 'numstarting', 'native': True}, 'numUnknown': {'type': 'int', 'name': 'numunknown', 'native': True}, 'numTemplates': {'type': 'int', 'name': 'numtemplates', 'native': True}, 'maxCount': {'type': 'int', 'name': 'maxcount', 'native': True}, 'minCount': {'type': 'int', 'name': 'mincount', 'native': True}, 'numRunning': {'type': 'int', 'name': 'numrunning', 'native': True}})
        self.numstarting = numstarting
        self.maxcount = maxcount
        self.numinstances = numinstances
        self.numdestroyed = numdestroyed
        self.numstopped = numstopped
        self.topologyid = topologyid
        self.numstopping = numstopping
        self.numfailed = numfailed
        self.numrunning = numrunning
        self.numunknown = numunknown
        self.numtemplates = numtemplates
        self.numdegraded = numdegraded
        self.mincount = mincount
        self.numpaused = numpaused 
