from base.Workload import WorkloadBase
from actions.Workload import WorkloadActions

class Workload(WorkloadBase, WorkloadActions):
    '''
    classdocs
    '''
    def __init__(self, releasedisks=None, numinstances=None, scaleuppolicy=None, scaledownpolicy=None, srcconnections=None, hostnameprefix=None, volumes=[], destconnections=None, packages=[], basestack=None, operatingsystem=None, resources=[], configurations=[]):
        '''
        Constructor
        @param releasedisks: releasedisks minOccurs=0
        @type releasedisks: boolean
        @param numinstances: numinstances
        @type numinstances: int
        @param scaleuppolicy: scaleuppolicy minOccurs=0
        @type scaleuppolicy: Policy
        @param scaledownpolicy: scaledownpolicy minOccurs=0
        @type scaledownpolicy: Policy
        @param srcconnections: srcconnections minOccurs=0
        @type srcconnections: Link
        @param hostnameprefix: hostnameprefix minOccurs=0
        @type hostnameprefix: string
        @param volumes: volumes minOccurs=0 maxOccurs=unbounded
        @type volumes: Volume
        @param destconnections: destconnections minOccurs=0
        @type destconnections: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param basestack: basestack minOccurs=0
        @type basestack: Link
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param configurations: configurations minOccurs=0 maxOccurs=unbounded
        @type configurations: Link
        '''
        WorkloadBase.__init__(self, releasedisks=releasedisks, numinstances=numinstances, scaleuppolicy=scaleuppolicy, scaledownpolicy=scaledownpolicy, srcconnections=srcconnections, hostnameprefix=hostnameprefix, volumes=volumes, destconnections=destconnections, packages=packages, basestack=basestack, operatingsystem=operatingsystem, resources=resources, configurations=configurations)
