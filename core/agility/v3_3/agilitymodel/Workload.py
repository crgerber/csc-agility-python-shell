from core.agility.v3_3.agilitymodel.base.Workload import WorkloadBase
from core.agility.v3_3.agilitymodel.actions.Workload import WorkloadActions

class Workload(WorkloadBase, WorkloadActions):
    '''
    classdocs
    '''
    def __init__(self, hostnameprefix=None, operatingsystem=None, srcconnections=None, destconnections=None, releasedisks=None, basestack=None, numinstances=None, scaleuppolicy=None, scaledownpolicy=None, configurations=[], packages=[], volumes=[], resources=[]):
        '''
        Constructor
        @param hostnameprefix: hostnameprefix minOccurs=0
        @type hostnameprefix: string
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param srcconnections: srcconnections minOccurs=0
        @type srcconnections: Link
        @param destconnections: destconnections minOccurs=0
        @type destconnections: Link
        @param releasedisks: releasedisks minOccurs=0
        @type releasedisks: boolean
        @param basestack: basestack minOccurs=0
        @type basestack: Link
        @param numinstances: numinstances
        @type numinstances: int
        @param scaleuppolicy: scaleuppolicy minOccurs=0
        @type scaleuppolicy: Policy
        @param scaledownpolicy: scaledownpolicy minOccurs=0
        @type scaledownpolicy: Policy
        @param configurations: configurations minOccurs=0 maxOccurs=unbounded
        @type configurations: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param volumes: volumes minOccurs=0 maxOccurs=unbounded
        @type volumes: Volume
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        '''
        WorkloadBase.__init__(self, hostnameprefix=hostnameprefix, operatingsystem=operatingsystem, srcconnections=srcconnections, destconnections=destconnections, releasedisks=releasedisks, basestack=basestack, numinstances=numinstances, scaleuppolicy=scaleuppolicy, scaledownpolicy=scaledownpolicy, configurations=configurations, packages=packages, volumes=volumes, resources=resources)
