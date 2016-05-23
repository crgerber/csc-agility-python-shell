from core.agility.v3_3.agilitymodel.base.TemplateStats import TemplateStatsBase
from core.agility.v3_3.agilitymodel.actions.TemplateStats import TemplateStatsActions

class TemplateStats(TemplateStatsBase, TemplateStatsActions):
    '''
    classdocs
    '''
    def __init__(self, numunknown=None, numfailed=None, numstopping=None, mincount=None, numpaused=None, numdegraded=None, numstopped=None, maxcount=None, templateid=None, numdestroyed=None, numstarting=None, numinstances=None, numrunning=None, status=''):
        '''
        Constructor
        @param numunknown: numunknown
        @type numunknown: int
        @param numfailed: numfailed
        @type numfailed: int
        @param numstopping: numstopping
        @type numstopping: int
        @param mincount: mincount
        @type mincount: int
        @param numpaused: numpaused
        @type numpaused: int
        @param numdegraded: numdegraded
        @type numdegraded: int
        @param numstopped: numstopped
        @type numstopped: int
        @param maxcount: maxcount
        @type maxcount: int
        @param templateid: templateid
        @type templateid: int
        @param numdestroyed: numdestroyed
        @type numdestroyed: int
        @param numstarting: numstarting
        @type numstarting: int
        @param numinstances: numinstances
        @type numinstances: int
        @param numrunning: numrunning
        @type numrunning: int
        @param status: status
        @type status: string
        '''
        TemplateStatsBase.__init__(self, numunknown=numunknown, numfailed=numfailed, numstopping=numstopping, mincount=mincount, numpaused=numpaused, numdegraded=numdegraded, numstopped=numstopped, maxcount=maxcount, templateid=templateid, numdestroyed=numdestroyed, numstarting=numstarting, numinstances=numinstances, numrunning=numrunning, status=status)
