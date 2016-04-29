from core.agility.common.AgilityModelBase import AgilityModelBase

class TopologyStatsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, numinstances=None, numstopping=None, numfailed=None, numstopped=None, status='', numrunning=None, numpaused=None, numserviceinstances=None, numstarting=None, numdestroyed=None, numunknown=None, topologyid=None, numdegraded=None, mincount=None, maxcount=None, numtemplates=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'numInstances': {'native': True, 'name': 'numinstances', 'type': 'int'}, 'numStopping': {'native': True, 'name': 'numstopping', 'type': 'int'}, 'numTemplates': {'native': True, 'name': 'numtemplates', 'type': 'int'}, 'numFailed': {'native': True, 'name': 'numfailed', 'type': 'int'}, 'numStopped': {'native': True, 'name': 'numstopped', 'type': 'int'}, 'status': {'native': True, 'name': 'status', 'type': 'string'}, 'numRunning': {'native': True, 'name': 'numrunning', 'type': 'int'}, 'numServiceInstances': {'native': True, 'name': 'numserviceinstances', 'type': 'int'}, 'numStarting': {'native': True, 'name': 'numstarting', 'type': 'int'}, 'numDestroyed': {'native': True, 'name': 'numdestroyed', 'type': 'int'}, 'numUnknown': {'native': True, 'name': 'numunknown', 'type': 'int'}, 'topologyId': {'native': True, 'name': 'topologyid', 'type': 'int'}, 'numPaused': {'native': True, 'name': 'numpaused', 'type': 'int'}, 'minCount': {'native': True, 'name': 'mincount', 'type': 'int'}, 'maxCount': {'native': True, 'name': 'maxcount', 'type': 'int'}, 'numDegraded': {'native': True, 'name': 'numdegraded', 'type': 'int'}})
        self.numinstances = numinstances
        self.numstopping = numstopping
        self.numfailed = numfailed
        self.numstopped = numstopped
        self.status = status
        self.numrunning = numrunning
        self.numpaused = numpaused
        self.numserviceinstances = numserviceinstances
        self.numstarting = numstarting
        self.numdestroyed = numdestroyed
        self.numunknown = numunknown
        self.topologyid = topologyid
        self.numdegraded = numdegraded
        self.mincount = mincount
        self.maxcount = maxcount
        self.numtemplates = numtemplates 
