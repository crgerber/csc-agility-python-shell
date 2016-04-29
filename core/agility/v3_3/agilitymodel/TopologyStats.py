from core.agility.v3_3.agilitymodel.base.TopologyStats import TopologyStatsBase
from core.agility.v3_3.agilitymodel.actions.TopologyStats import TopologyStatsActions

class TopologyStats(TopologyStatsBase, TopologyStatsActions):
    '''
    classdocs
    '''
    def __init__(self, numinstances=None, numstopping=None, numfailed=None, numstopped=None, status='', numrunning=None, numpaused=None, numserviceinstances=None, numstarting=None, numdestroyed=None, numunknown=None, topologyid=None, numdegraded=None, mincount=None, maxcount=None, numtemplates=None):
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
        @param numserviceinstances: numserviceinstances
        @type numserviceinstances: int
        @param numstarting: numstarting
        @type numstarting: int
        @param numdestroyed: numdestroyed
        @type numdestroyed: int
        @param numunknown: numunknown
        @type numunknown: int
        @param topologyid: topologyid
        @type topologyid: int
        @param numdegraded: numdegraded
        @type numdegraded: int
        @param mincount: mincount
        @type mincount: int
        @param maxcount: maxcount
        @type maxcount: int
        @param numtemplates: numtemplates
        @type numtemplates: int
        '''
        TopologyStatsBase.__init__(self, numinstances=numinstances, numstopping=numstopping, numfailed=numfailed, numstopped=numstopped, status=status, numrunning=numrunning, numpaused=numpaused, numserviceinstances=numserviceinstances, numstarting=numstarting, numdestroyed=numdestroyed, numunknown=numunknown, topologyid=topologyid, numdegraded=numdegraded, mincount=mincount, maxcount=maxcount, numtemplates=numtemplates)
