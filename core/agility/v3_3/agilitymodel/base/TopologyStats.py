from core.agility.common.AgilityModelBase import AgilityModelBase

class TopologyStatsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, maxcount=None, numunknown=None, topologyid=None, numtemplates=None, numstopping=None, mincount=None, numpaused=None, numdegraded=None, numdestroyed=None, numserviceinstances=None, numfailed=None, numstopped=None, numstarting=None, numinstances=None, numrunning=None, status=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'numRunning': {'name': 'numrunning', 'native': True, 'type': 'int'}, 'numUnknown': {'name': 'numunknown', 'native': True, 'type': 'int'}, 'numFailed': {'name': 'numfailed', 'native': True, 'type': 'int'}, 'numTemplates': {'name': 'numtemplates', 'native': True, 'type': 'int'}, 'topologyId': {'name': 'topologyid', 'native': True, 'type': 'int'}, 'minCount': {'name': 'mincount', 'native': True, 'type': 'int'}, 'numPaused': {'name': 'numpaused', 'native': True, 'type': 'int'}, 'numDegraded': {'name': 'numdegraded', 'native': True, 'type': 'int'}, 'numDestroyed': {'name': 'numdestroyed', 'native': True, 'type': 'int'}, 'numServiceInstances': {'name': 'numserviceinstances', 'native': True, 'type': 'int'}, 'numStopped': {'name': 'numstopped', 'native': True, 'type': 'int'}, 'numStarting': {'name': 'numstarting', 'native': True, 'type': 'int'}, 'numStopping': {'name': 'numstopping', 'native': True, 'type': 'int'}, 'numInstances': {'name': 'numinstances', 'native': True, 'type': 'int'}, 'maxCount': {'name': 'maxcount', 'native': True, 'type': 'int'}, 'status': {'name': 'status', 'native': True, 'type': 'string'}})
        self.maxcount = maxcount
        self.numunknown = numunknown
        self.topologyid = topologyid
        self.numtemplates = numtemplates
        self.numstopping = numstopping
        self.mincount = mincount
        self.numpaused = numpaused
        self.numdegraded = numdegraded
        self.numdestroyed = numdestroyed
        self.numserviceinstances = numserviceinstances
        self.numfailed = numfailed
        self.numstopped = numstopped
        self.numstarting = numstarting
        self.numinstances = numinstances
        self.numrunning = numrunning
        self.status = status 
