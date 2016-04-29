from core.agility.v3_3.agilitymodel.base.Workload import WorkloadBase
from core.agility.v3_3.agilitymodel.actions.Workload import WorkloadActions

class Workload(WorkloadBase, WorkloadActions):
    '''
    classdocs
    '''
    def __init__(self, numinstances=None, destconnections=None, volumes=[], configurations=[], releasedisks=None, scaleuppolicy=None, resources=[], hostnameprefix=None, basestack=None, scaledownpolicy=None, operatingsystem=None, packages=[], srcconnections=None):
        '''
        Constructor
        @param numinstances: numinstances
        @type numinstances: int
        @param destconnections: destconnections minOccurs=0
        @type destconnections: Link
        @param volumes: volumes minOccurs=0 maxOccurs=unbounded
        @type volumes: Volume
        @param configurations: configurations minOccurs=0 maxOccurs=unbounded
        @type configurations: Link
        @param releasedisks: releasedisks minOccurs=0
        @type releasedisks: boolean
        @param scaleuppolicy: scaleuppolicy minOccurs=0
        @type scaleuppolicy: Policy
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param hostnameprefix: hostnameprefix minOccurs=0
        @type hostnameprefix: string
        @param basestack: basestack minOccurs=0
        @type basestack: Link
        @param scaledownpolicy: scaledownpolicy minOccurs=0
        @type scaledownpolicy: Policy
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param srcconnections: srcconnections minOccurs=0
        @type srcconnections: Link
        '''
        WorkloadBase.__init__(self, numinstances=numinstances, destconnections=destconnections, volumes=volumes, configurations=configurations, releasedisks=releasedisks, scaleuppolicy=scaleuppolicy, resources=resources, hostnameprefix=hostnameprefix, basestack=basestack, scaledownpolicy=scaledownpolicy, operatingsystem=operatingsystem, packages=packages, srcconnections=srcconnections)
