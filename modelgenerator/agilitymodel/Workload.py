from base.Workload import WorkloadBase
from actions.Workload import WorkloadActions

class Workload(WorkloadBase, WorkloadActions):
    '''
    classdocs
    '''
    def __init__(self, numInstances=None, scaleUpPolicy=None, scaleDownPolicy=None, srcConnections=None, hostnamePrefix=None, volumes=list(), destConnections=None, packages=list(), baseStack=None, operatingSystem=None, resources=list(), configurations=list()):
        '''
        Constructor
        @param numInstances: numInstances
        @type numInstances: int
        @param scaleUpPolicy: scaleUpPolicy minOccurs=0
        @type scaleUpPolicy: Policy
        @param scaleDownPolicy: scaleDownPolicy minOccurs=0
        @type scaleDownPolicy: Policy
        @param srcConnections: srcConnections minOccurs=0
        @type srcConnections: Link
        @param hostnamePrefix: hostnamePrefix minOccurs=0
        @type hostnamePrefix: string
        @param volumes: volumes minOccurs=0 maxOccurs=unbounded
        @type volumes: Volume
        @param destConnections: destConnections minOccurs=0
        @type destConnections: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param baseStack: baseStack minOccurs=0
        @type baseStack: Link
        @param operatingSystem: operatingSystem minOccurs=0
        @type operatingSystem: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param configurations: configurations minOccurs=0 maxOccurs=unbounded
        @type configurations: Link
        '''
        WorkloadBase.__init__(self, numInstances=numInstances, scaleUpPolicy=scaleUpPolicy, scaleDownPolicy=scaleDownPolicy, srcConnections=srcConnections, hostnamePrefix=hostnamePrefix, volumes=volumes, destConnections=destConnections, packages=packages, baseStack=baseStack, operatingSystem=operatingSystem, resources=resources, configurations=configurations)
