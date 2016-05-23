from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class InstanceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, starttime=None, onboarded=None, location=None, stoptime=None, scriptstatuslink=[], model=None, pending=None, cloud=None, variables=[], publicaddress=None, snapshots=[], resources=[], privateaddress=None, lastupdate=None, canonicalname=None, properties=[], environment=None, template=None, volumestorage=[], instanceid=None, stack=None, hostname=None, addresses=[], state=None, scriptstatus=[], laststartedorstoppedby=None, createdon=None, credential=[], image=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'startTime': {'name': 'starttime', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'onboarded': {'name': 'onboarded', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'location': {'name': 'location', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'stopTime': {'name': 'stoptime', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'scriptstatusLink': {'name': 'scriptstatuslink', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'model': {'name': 'model', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'pending': {'name': 'pending', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'template': {'name': 'template', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'snapshots': {'name': 'snapshots', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Snapshot'}, 'resources': {'name': 'resources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Resource'}, 'privateAddress': {'name': 'privateaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'lastUpdate': {'name': 'lastupdate', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'canonicalName': {'name': 'canonicalname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'environment': {'name': 'environment', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'publicAddress': {'name': 'publicaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'volumeStorage': {'name': 'volumestorage', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'instanceId': {'name': 'instanceid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'stack': {'name': 'stack', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'hostname': {'name': 'hostname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'addresses': {'name': 'addresses', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Address'}, 'state': {'name': 'state', 'minOccurs': '0', 'native': False, 'type': 'State'}, 'scriptstatus': {'name': 'scriptstatus', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ScriptStatus'}, 'createdOn': {'name': 'createdon', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'lastStartedOrStoppedBy': {'name': 'laststartedorstoppedby', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'credential': {'name': 'credential', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'image': {'name': 'image', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.starttime = starttime
        self.onboarded = onboarded
        self.location = location
        self.stoptime = stoptime
        self.scriptstatuslink = scriptstatuslink
        self.model = model
        self.pending = pending
        self.cloud = cloud
        self.variables = variables
        self.publicaddress = publicaddress
        self.snapshots = snapshots
        self.resources = resources
        self.privateaddress = privateaddress
        self.lastupdate = lastupdate
        self.canonicalname = canonicalname
        self.properties = properties
        self.environment = environment
        self.template = template
        self.volumestorage = volumestorage
        self.instanceid = instanceid
        self.stack = stack
        self.hostname = hostname
        self.addresses = addresses
        self.state = state
        self.scriptstatus = scriptstatus
        self.laststartedorstoppedby = laststartedorstoppedby
        self.createdon = createdon
        self.credential = credential
        self.image = image 
