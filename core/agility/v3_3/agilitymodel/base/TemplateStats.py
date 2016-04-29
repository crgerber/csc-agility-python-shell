from core.agility.common.AgilityModelBase import AgilityModelBase

class TemplateStatsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, numinstances=None, numstopping=None, numfailed=None, numstopped=None, status='', numrunning=None, numpaused=None, templateid=None, numstarting=None, numdestroyed=None, numunknown=None, numdegraded=None, maxcount=None, mincount=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'numInstances': {'native': True, 'name': 'numinstances', 'type': 'int'}, 'numStopping': {'native': True, 'name': 'numstopping', 'type': 'int'}, 'numFailed': {'native': True, 'name': 'numfailed', 'type': 'int'}, 'numStopped': {'native': True, 'name': 'numstopped', 'type': 'int'}, 'status': {'native': True, 'name': 'status', 'type': 'string'}, 'numRunning': {'native': True, 'name': 'numrunning', 'type': 'int'}, 'numPaused': {'native': True, 'name': 'numpaused', 'type': 'int'}, 'templateId': {'native': True, 'name': 'templateid', 'type': 'int'}, 'numStarting': {'native': True, 'name': 'numstarting', 'type': 'int'}, 'numDestroyed': {'native': True, 'name': 'numdestroyed', 'type': 'int'}, 'numUnknown': {'native': True, 'name': 'numunknown', 'type': 'int'}, 'numDegraded': {'native': True, 'name': 'numdegraded', 'type': 'int'}, 'maxCount': {'native': True, 'name': 'maxcount', 'type': 'int'}, 'minCount': {'native': True, 'name': 'mincount', 'type': 'int'}})
        self.numinstances = numinstances
        self.numstopping = numstopping
        self.numfailed = numfailed
        self.numstopped = numstopped
        self.status = status
        self.numrunning = numrunning
        self.numpaused = numpaused
        self.templateid = templateid
        self.numstarting = numstarting
        self.numdestroyed = numdestroyed
        self.numunknown = numunknown
        self.numdegraded = numdegraded
        self.maxcount = maxcount
        self.mincount = mincount 
