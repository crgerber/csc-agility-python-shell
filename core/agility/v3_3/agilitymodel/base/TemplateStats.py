from core.agility.common.AgilityModelBase import AgilityModelBase

class TemplateStatsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status='', maxcount=None, numdegraded=None, numinstances=None, numrunning=None, numstopped=None, numstopping=None, numfailed=None, numpaused=None, numunknown=None, templateid=None, mincount=None, numstarting=None, numdestroyed=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'native': True}, 'numStopping': {'type': 'int', 'name': 'numstopping', 'native': True}, 'numInstances': {'type': 'int', 'name': 'numinstances', 'native': True}, 'numDestroyed': {'type': 'int', 'name': 'numdestroyed', 'native': True}, 'numDegraded': {'type': 'int', 'name': 'numdegraded', 'native': True}, 'maxCount': {'type': 'int', 'name': 'maxcount', 'native': True}, 'numFailed': {'type': 'int', 'name': 'numfailed', 'native': True}, 'numRunning': {'type': 'int', 'name': 'numrunning', 'native': True}, 'numUnknown': {'type': 'int', 'name': 'numunknown', 'native': True}, 'numStopped': {'type': 'int', 'name': 'numstopped', 'native': True}, 'minCount': {'type': 'int', 'name': 'mincount', 'native': True}, 'numPaused': {'type': 'int', 'name': 'numpaused', 'native': True}, 'numStarting': {'type': 'int', 'name': 'numstarting', 'native': True}, 'templateId': {'type': 'int', 'name': 'templateid', 'native': True}})
        self.status = status
        self.maxcount = maxcount
        self.numdegraded = numdegraded
        self.numinstances = numinstances
        self.numrunning = numrunning
        self.numstopped = numstopped
        self.numstopping = numstopping
        self.numfailed = numfailed
        self.numpaused = numpaused
        self.numunknown = numunknown
        self.templateid = templateid
        self.mincount = mincount
        self.numstarting = numstarting
        self.numdestroyed = numdestroyed 
