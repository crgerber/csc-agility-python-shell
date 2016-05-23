from core.agility.v3_3.agilitymodel.base.TopologyStats import TopologyStatsBase
from core.agility.v3_3.agilitymodel.actions.TopologyStats import TopologyStatsActions

class TopologyStats(TopologyStatsBase, TopologyStatsActions):
    '''
    classdocs
    '''
    def __init__(self, maxcount=None, numunknown=None, topologyid=None, numtemplates=None, numstopping=None, mincount=None, numpaused=None, numdegraded=None, numdestroyed=None, numserviceinstances=None, numfailed=None, numstopped=None, numstarting=None, numinstances=None, numrunning=None, status=''):
        '''
        Constructor
        @param maxcount: maxcount
        @type maxcount: int
        @param numunknown: numunknown
        @type numunknown: int
        @param topologyid: topologyid
        @type topologyid: int
        @param numtemplates: numtemplates
        @type numtemplates: int
        @param numstopping: numstopping
        @type numstopping: int
        @param mincount: mincount
        @type mincount: int
        @param numpaused: numpaused
        @type numpaused: int
        @param numdegraded: numdegraded
        @type numdegraded: int
        @param numdestroyed: numdestroyed
        @type numdestroyed: int
        @param numserviceinstances: numserviceinstances
        @type numserviceinstances: int
        @param numfailed: numfailed
        @type numfailed: int
        @param numstopped: numstopped
        @type numstopped: int
        @param numstarting: numstarting
        @type numstarting: int
        @param numinstances: numinstances
        @type numinstances: int
        @param numrunning: numrunning
        @type numrunning: int
        @param status: status
        @type status: string
        '''
        TopologyStatsBase.__init__(self, maxcount=maxcount, numunknown=numunknown, topologyid=topologyid, numtemplates=numtemplates, numstopping=numstopping, mincount=mincount, numpaused=numpaused, numdegraded=numdegraded, numdestroyed=numdestroyed, numserviceinstances=numserviceinstances, numfailed=numfailed, numstopped=numstopped, numstarting=numstarting, numinstances=numinstances, numrunning=numrunning, status=status)
