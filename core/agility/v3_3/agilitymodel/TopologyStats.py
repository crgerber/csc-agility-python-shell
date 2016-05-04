from core.agility.v3_3.agilitymodel.base.TopologyStats import TopologyStatsBase
from core.agility.v3_3.agilitymodel.actions.TopologyStats import TopologyStatsActions

class TopologyStats(TopologyStatsBase, TopologyStatsActions):
    '''
    classdocs
    '''
    def __init__(self, numstarting=None, numserviceinstances=None, maxcount=None, numinstances=None, numdestroyed=None, numstopped=None, topologyid=None, numstopping=None, numfailed=None, numrunning=None, status='', numunknown=None, numtemplates=None, numdegraded=None, mincount=None, numpaused=None):
        '''
        Constructor
        @param numstarting: numstarting
        @type numstarting: int
        @param numserviceinstances: numserviceinstances
        @type numserviceinstances: int
        @param maxcount: maxcount
        @type maxcount: int
        @param numinstances: numinstances
        @type numinstances: int
        @param numdestroyed: numdestroyed
        @type numdestroyed: int
        @param numstopped: numstopped
        @type numstopped: int
        @param topologyid: topologyid
        @type topologyid: int
        @param numstopping: numstopping
        @type numstopping: int
        @param numfailed: numfailed
        @type numfailed: int
        @param numrunning: numrunning
        @type numrunning: int
        @param status: status
        @type status: string
        @param numunknown: numunknown
        @type numunknown: int
        @param numtemplates: numtemplates
        @type numtemplates: int
        @param numdegraded: numdegraded
        @type numdegraded: int
        @param mincount: mincount
        @type mincount: int
        @param numpaused: numpaused
        @type numpaused: int
        '''
        TopologyStatsBase.__init__(self, numstarting=numstarting, numserviceinstances=numserviceinstances, maxcount=maxcount, numinstances=numinstances, numdestroyed=numdestroyed, numstopped=numstopped, topologyid=topologyid, numstopping=numstopping, numfailed=numfailed, numrunning=numrunning, status=status, numunknown=numunknown, numtemplates=numtemplates, numdegraded=numdegraded, mincount=mincount, numpaused=numpaused)
