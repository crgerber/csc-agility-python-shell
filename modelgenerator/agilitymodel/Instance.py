from base.Instance import InstanceBase
from actions.Instance import InstanceActions

class Instance(InstanceBase, InstanceActions):
    '''
    classdocs
    '''
    def __init__(self, addresses=list(), lastUpdate=None, instanceId=None, variables=list(), snapshots=list(), cloud=None, publicAddress=None, hostname=None, stack=None, environment=None, state=None, stopTime=None, template=None, scriptstatus=list(), privateAddress=None, resources=list(), volumeStorage=list(), credential=list(), canonicalName=None, startTime=None, properties=list(), createdOn=None, onboarded=None):
        '''
        Constructor
        @param addresses: addresses minOccurs=0 maxOccurs=unbounded
        @type addresses: Address
        @param lastUpdate: lastUpdate minOccurs=0
        @type lastUpdate: date
        @param instanceId: instanceId minOccurs=0
        @type instanceId: string
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param snapshots: snapshots minOccurs=0 maxOccurs=unbounded
        @type snapshots: Snapshot
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param publicAddress: publicAddress minOccurs=0
        @type publicAddress: string
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param stack: stack minOccurs=0
        @type stack: Link
        @param environment: environment minOccurs=0
        @type environment: Link
        @param state: state minOccurs=0
        @type state: State
        @param stopTime: stopTime minOccurs=0
        @type stopTime: date
        @param template: template minOccurs=0
        @type template: Link
        @param scriptstatus: scriptstatus minOccurs=0 maxOccurs=unbounded
        @type scriptstatus: ScriptStatus
        @param privateAddress: privateAddress minOccurs=0
        @type privateAddress: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param volumeStorage: volumeStorage minOccurs=0 maxOccurs=unbounded
        @type volumeStorage: Link
        @param credential: credential minOccurs=0 maxOccurs=unbounded
        @type credential: Link
        @param canonicalName: canonicalName minOccurs=0
        @type canonicalName: string
        @param startTime: startTime minOccurs=0
        @type startTime: date
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param createdOn: createdOn minOccurs=0
        @type createdOn: date
        @param onboarded: onboarded minOccurs=0
        @type onboarded: boolean
        '''
        InstanceBase.__init__(self, addresses=addresses, lastUpdate=lastUpdate, instanceId=instanceId, variables=variables, snapshots=snapshots, cloud=cloud, publicAddress=publicAddress, hostname=hostname, stack=stack, environment=environment, state=state, stopTime=stopTime, template=template, scriptstatus=scriptstatus, privateAddress=privateAddress, resources=resources, volumeStorage=volumeStorage, credential=credential, canonicalName=canonicalName, startTime=startTime, properties=properties, createdOn=createdOn, onboarded=onboarded)
