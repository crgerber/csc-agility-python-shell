from core.agility.common.AgilityModelBase import AgilityModelBase

class TemplateStatsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, numunknown=None, numfailed=None, numstopping=None, mincount=None, numpaused=None, numdegraded=None, numstopped=None, maxcount=None, templateid=None, numdestroyed=None, numstarting=None, numinstances=None, numrunning=None, status=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'numUnknown': {'name': 'numunknown', 'native': True, 'type': 'int'}, 'numFailed': {'name': 'numfailed', 'native': True, 'type': 'int'}, 'numStopping': {'name': 'numstopping', 'native': True, 'type': 'int'}, 'minCount': {'name': 'mincount', 'native': True, 'type': 'int'}, 'numPaused': {'name': 'numpaused', 'native': True, 'type': 'int'}, 'numDegraded': {'name': 'numdegraded', 'native': True, 'type': 'int'}, 'numDestroyed': {'name': 'numdestroyed', 'native': True, 'type': 'int'}, 'numRunning': {'name': 'numrunning', 'native': True, 'type': 'int'}, 'templateId': {'name': 'templateid', 'native': True, 'type': 'int'}, 'numStopped': {'name': 'numstopped', 'native': True, 'type': 'int'}, 'numStarting': {'name': 'numstarting', 'native': True, 'type': 'int'}, 'numInstances': {'name': 'numinstances', 'native': True, 'type': 'int'}, 'maxCount': {'name': 'maxcount', 'native': True, 'type': 'int'}, 'status': {'name': 'status', 'native': True, 'type': 'string'}})
        self.numunknown = numunknown
        self.numfailed = numfailed
        self.numstopping = numstopping
        self.mincount = mincount
        self.numpaused = numpaused
        self.numdegraded = numdegraded
        self.numstopped = numstopped
        self.maxcount = maxcount
        self.templateid = templateid
        self.numdestroyed = numdestroyed
        self.numstarting = numstarting
        self.numinstances = numinstances
        self.numrunning = numrunning
        self.status = status 
