from core.agility.v3_3.agilitymodel.base.TemplateStats import TemplateStatsBase
from core.agility.v3_3.agilitymodel.actions.TemplateStats import TemplateStatsActions

class TemplateStats(TemplateStatsBase, TemplateStatsActions):
    '''
    classdocs
    '''
    def __init__(self, numinstances=None, numstopping=None, numfailed=None, numstopped=None, status='', numrunning=None, numpaused=None, templateid=None, numstarting=None, numdestroyed=None, numunknown=None, numdegraded=None, maxcount=None, mincount=None):
        '''
        Constructor
        @param numinstances: numinstances
        @type numinstances: int
        @param numstopping: numstopping
        @type numstopping: int
        @param numfailed: numfailed
        @type numfailed: int
        @param numstopped: numstopped
        @type numstopped: int
        @param status: status
        @type status: string
        @param numrunning: numrunning
        @type numrunning: int
        @param numpaused: numpaused
        @type numpaused: int
        @param templateid: templateid
        @type templateid: int
        @param numstarting: numstarting
        @type numstarting: int
        @param numdestroyed: numdestroyed
        @type numdestroyed: int
        @param numunknown: numunknown
        @type numunknown: int
        @param numdegraded: numdegraded
        @type numdegraded: int
        @param maxcount: maxcount
        @type maxcount: int
        @param mincount: mincount
        @type mincount: int
        '''
        TemplateStatsBase.__init__(self, numinstances=numinstances, numstopping=numstopping, numfailed=numfailed, numstopped=numstopped, status=status, numrunning=numrunning, numpaused=numpaused, templateid=templateid, numstarting=numstarting, numdestroyed=numdestroyed, numunknown=numunknown, numdegraded=numdegraded, maxcount=maxcount, mincount=mincount)
