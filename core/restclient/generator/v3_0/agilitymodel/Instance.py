from base.Instance import InstanceBase
from actions.Instance import InstanceActions

class Instance(InstanceBase, InstanceActions):
    '''
    classdocs
    '''
    def __init__(self, addresses=[], lastupdate=None, instanceid=None, variables=[], snapshots=[], cloud=None, publicaddress=None, image=None, hostname=None, stack=None, environment=None, state=None, stoptime=None, location=None, template=None, scriptstatus=[], privateaddress=None, resources=[], volumestorage=[], credential=[], canonicalname=None, starttime=None, properties=[], createdon=None, model=None, onboarded=None):
        '''
        Constructor
        @param addresses: addresses minOccurs=0 maxOccurs=unbounded
        @type addresses: Address
        @param lastupdate: lastupdate minOccurs=0
        @type lastupdate: date
        @param instanceid: instanceid minOccurs=0
        @type instanceid: string
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param snapshots: snapshots minOccurs=0 maxOccurs=unbounded
        @type snapshots: Snapshot
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param publicaddress: publicaddress minOccurs=0
        @type publicaddress: string
        @param image: image minOccurs=0
        @type image: Link
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param stack: stack minOccurs=0
        @type stack: Link
        @param environment: environment minOccurs=0
        @type environment: Link
        @param state: state minOccurs=0
        @type state: State
        @param stoptime: stoptime minOccurs=0
        @type stoptime: date
        @param location: location minOccurs=0
        @type location: Link
        @param template: template minOccurs=0
        @type template: Link
        @param scriptstatus: scriptstatus minOccurs=0 maxOccurs=unbounded
        @type scriptstatus: ScriptStatus
        @param privateaddress: privateaddress minOccurs=0
        @type privateaddress: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param volumestorage: volumestorage minOccurs=0 maxOccurs=unbounded
        @type volumestorage: Link
        @param credential: credential minOccurs=0 maxOccurs=unbounded
        @type credential: Link
        @param canonicalname: canonicalname minOccurs=0
        @type canonicalname: string
        @param starttime: starttime minOccurs=0
        @type starttime: date
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param createdon: createdon minOccurs=0
        @type createdon: date
        @param model: model minOccurs=0
        @type model: Link
        @param onboarded: onboarded minOccurs=0
        @type onboarded: boolean
        '''
        InstanceBase.__init__(self, addresses=addresses, lastupdate=lastupdate, instanceid=instanceid, variables=variables, snapshots=snapshots, cloud=cloud, publicaddress=publicaddress, image=image, hostname=hostname, stack=stack, environment=environment, state=state, stoptime=stoptime, location=location, template=template, scriptstatus=scriptstatus, privateaddress=privateaddress, resources=resources, volumestorage=volumestorage, credential=credential, canonicalname=canonicalname, starttime=starttime, properties=properties, createdon=createdon, model=model, onboarded=onboarded)
