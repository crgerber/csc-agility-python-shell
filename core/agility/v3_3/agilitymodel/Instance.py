from core.agility.v3_3.agilitymodel.base.Instance import InstanceBase
from core.agility.v3_3.agilitymodel.actions.Instance import InstanceActions

class Instance(InstanceBase, InstanceActions):
    '''
    classdocs
    '''
    def __init__(self, starttime=None, onboarded=None, location=None, stoptime=None, scriptstatuslink=[], model=None, pending=None, cloud=None, variables=[], publicaddress=None, snapshots=[], resources=[], privateaddress=None, lastupdate=None, canonicalname=None, properties=[], environment=None, template=None, volumestorage=[], instanceid=None, stack=None, hostname=None, addresses=[], state=None, scriptstatus=[], laststartedorstoppedby=None, createdon=None, credential=[], image=None):
        '''
        Constructor
        @param starttime: starttime minOccurs=0
        @type starttime: date
        @param onboarded: onboarded minOccurs=0
        @type onboarded: boolean
        @param location: location minOccurs=0
        @type location: Link
        @param stoptime: stoptime minOccurs=0
        @type stoptime: date
        @param scriptstatuslink: scriptstatuslink minOccurs=0 maxOccurs=unbounded
        @type scriptstatuslink: Link
        @param model: model minOccurs=0
        @type model: Link
        @param pending: pending minOccurs=0
        @type pending: boolean
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param publicaddress: publicaddress minOccurs=0
        @type publicaddress: string
        @param snapshots: snapshots minOccurs=0 maxOccurs=unbounded
        @type snapshots: Snapshot
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param privateaddress: privateaddress minOccurs=0
        @type privateaddress: string
        @param lastupdate: lastupdate minOccurs=0
        @type lastupdate: date
        @param canonicalname: canonicalname minOccurs=0
        @type canonicalname: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param environment: environment minOccurs=0
        @type environment: Link
        @param template: template minOccurs=0
        @type template: Link
        @param volumestorage: volumestorage minOccurs=0 maxOccurs=unbounded
        @type volumestorage: Link
        @param instanceid: instanceid minOccurs=0
        @type instanceid: string
        @param stack: stack minOccurs=0
        @type stack: Link
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param addresses: addresses minOccurs=0 maxOccurs=unbounded
        @type addresses: Address
        @param state: state minOccurs=0
        @type state: State
        @param scriptstatus: scriptstatus minOccurs=0 maxOccurs=unbounded
        @type scriptstatus: ScriptStatus
        @param laststartedorstoppedby: laststartedorstoppedby minOccurs=0
        @type laststartedorstoppedby: string
        @param createdon: createdon minOccurs=0
        @type createdon: date
        @param credential: credential minOccurs=0 maxOccurs=unbounded
        @type credential: Link
        @param image: image minOccurs=0
        @type image: Link
        '''
        InstanceBase.__init__(self, starttime=starttime, onboarded=onboarded, location=location, stoptime=stoptime, scriptstatuslink=scriptstatuslink, model=model, pending=pending, cloud=cloud, variables=variables, publicaddress=publicaddress, snapshots=snapshots, resources=resources, privateaddress=privateaddress, lastupdate=lastupdate, canonicalname=canonicalname, properties=properties, environment=environment, template=template, volumestorage=volumestorage, instanceid=instanceid, stack=stack, hostname=hostname, addresses=addresses, state=state, scriptstatus=scriptstatus, laststartedorstoppedby=laststartedorstoppedby, createdon=createdon, credential=credential, image=image)
