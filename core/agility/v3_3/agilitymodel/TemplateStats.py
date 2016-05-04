from base.TemplateStats import TemplateStatsBase
from actions.TemplateStats import TemplateStatsActions

class TemplateStats(TemplateStatsBase, TemplateStatsActions):
    '''
    classdocs
    '''
    def __init__(self, status='', maxcount=None, numdegraded=None, numinstances=None, numrunning=None, numstopped=None, numstopping=None, numfailed=None, numpaused=None, numunknown=None, templateid=None, mincount=None, numstarting=None, numdestroyed=None):
        '''
        Constructor
        @param status: status
        @type status: string
        @param maxcount: maxcount
        @type maxcount: int
        @param numdegraded: numdegraded
        @type numdegraded: int
        @param numinstances: numinstances
        @type numinstances: int
        @param numrunning: numrunning
        @type numrunning: int
        @param numstopped: numstopped
        @type numstopped: int
        @param numstopping: numstopping
        @type numstopping: int
        @param numfailed: numfailed
        @type numfailed: int
        @param numpaused: numpaused
        @type numpaused: int
        @param numunknown: numunknown
        @type numunknown: int
        @param templateid: templateid
        @type templateid: int
        @param mincount: mincount
        @type mincount: int
        @param numstarting: numstarting
        @type numstarting: int
        @param numdestroyed: numdestroyed
        @type numdestroyed: int
        '''
        TemplateStatsBase.__init__(self, status=status, maxcount=maxcount, numdegraded=numdegraded, numinstances=numinstances, numrunning=numrunning, numstopped=numstopped, numstopping=numstopping, numfailed=numfailed, numpaused=numpaused, numunknown=numunknown, templateid=templateid, mincount=mincount, numstarting=numstarting, numdestroyed=numdestroyed)
