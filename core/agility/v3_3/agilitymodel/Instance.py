from core.agility.v3_3.agilitymodel.base.Instance import InstanceBase
from core.agility.v3_3.agilitymodel.actions.Instance import InstanceActions

class Instance(InstanceBase, InstanceActions):
    '''
    classdocs
    '''
    def __init__(self, scriptstatuslink=[], location=None, resources=[], pending=None, canonicalname=None, image=None, createdon=None, addresses=[], privateaddress=None, scriptstatus=[], variables=[], credential=[], template=None, model=None, properties=[], laststartedorstoppedby=None, instanceid=None, state=None, snapshots=[], starttime=None, lastupdate=None, environment=None, onboarded=None, stoptime=None, cloud=None, stack=None, hostname=None, volumestorage=[], publicaddress=None):
        '''
        Constructor
        @param scriptstatuslink: scriptstatuslink minOccurs=0 maxOccurs=unbounded
        @type scriptstatuslink: Link
        @param location: location minOccurs=0
        @type location: Link
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param pending: pending minOccurs=0
        @type pending: boolean
        @param canonicalname: canonicalname minOccurs=0
        @type canonicalname: string
        @param image: image minOccurs=0
        @type image: Link
        @param createdon: createdon minOccurs=0
        @type createdon: date
        @param addresses: addresses minOccurs=0 maxOccurs=unbounded
        @type addresses: Address
        @param privateaddress: privateaddress minOccurs=0
        @type privateaddress: string
        @param scriptstatus: scriptstatus minOccurs=0 maxOccurs=unbounded
        @type scriptstatus: ScriptStatus
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param credential: credential minOccurs=0 maxOccurs=unbounded
        @type credential: Link
        @param template: template minOccurs=0
        @type template: Link
        @param model: model minOccurs=0
        @type model: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param laststartedorstoppedby: laststartedorstoppedby minOccurs=0
        @type laststartedorstoppedby: string
        @param instanceid: instanceid minOccurs=0
        @type instanceid: string
        @param state: state minOccurs=0
        @type state: State
        @param snapshots: snapshots minOccurs=0 maxOccurs=unbounded
        @type snapshots: Snapshot
        @param starttime: starttime minOccurs=0
        @type starttime: date
        @param lastupdate: lastupdate minOccurs=0
        @type lastupdate: date
        @param environment: environment minOccurs=0
        @type environment: Link
        @param onboarded: onboarded minOccurs=0
        @type onboarded: boolean
        @param stoptime: stoptime minOccurs=0
        @type stoptime: date
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param stack: stack minOccurs=0
        @type stack: Link
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param volumestorage: volumestorage minOccurs=0 maxOccurs=unbounded
        @type volumestorage: Link
        @param publicaddress: publicaddress minOccurs=0
        @type publicaddress: string
        '''
        InstanceBase.__init__(self, scriptstatuslink=scriptstatuslink, location=location, resources=resources, pending=pending, canonicalname=canonicalname, image=image, createdon=createdon, addresses=addresses, privateaddress=privateaddress, scriptstatus=scriptstatus, variables=variables, credential=credential, template=template, model=model, properties=properties, laststartedorstoppedby=laststartedorstoppedby, instanceid=instanceid, state=state, snapshots=snapshots, starttime=starttime, lastupdate=lastupdate, environment=environment, onboarded=onboarded, stoptime=stoptime, cloud=cloud, stack=stack, hostname=hostname, volumestorage=volumestorage, publicaddress=publicaddress)
