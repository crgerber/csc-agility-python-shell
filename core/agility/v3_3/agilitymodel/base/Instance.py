from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class InstanceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, scriptstatuslink=[], location=None, resources=[], pending=None, canonicalname=None, image=None, createdon=None, addresses=[], privateaddress=None, scriptstatus=[], variables=[], credential=[], template=None, model=None, properties=[], laststartedorstoppedby=None, instanceid=None, state=None, snapshots=[], starttime=None, lastupdate=None, environment=None, onboarded=None, stoptime=None, cloud=None, stack=None, hostname=None, volumestorage=[], publicaddress=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'scriptstatusLink': {'maxOccurs': 'unbounded', 'native': False, 'name': 'scriptstatuslink', 'minOccurs': '0', 'type': 'Link'}, 'credential': {'maxOccurs': 'unbounded', 'native': False, 'name': 'credential', 'minOccurs': '0', 'type': 'Link'}, 'resources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resources', 'minOccurs': '0', 'type': 'Resource'}, 'pending': {'native': True, 'name': 'pending', 'minOccurs': '0', 'type': 'boolean'}, 'canonicalName': {'native': True, 'name': 'canonicalname', 'minOccurs': '0', 'type': 'string'}, 'stopTime': {'native': True, 'name': 'stoptime', 'minOccurs': '0', 'type': 'date'}, 'addresses': {'maxOccurs': 'unbounded', 'native': False, 'name': 'addresses', 'minOccurs': '0', 'type': 'Address'}, 'privateAddress': {'native': True, 'name': 'privateaddress', 'minOccurs': '0', 'type': 'string'}, 'scriptstatus': {'maxOccurs': 'unbounded', 'native': False, 'name': 'scriptstatus', 'minOccurs': '0', 'type': 'ScriptStatus'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}, 'location': {'native': False, 'name': 'location', 'minOccurs': '0', 'type': 'Link'}, 'template': {'native': False, 'name': 'template', 'minOccurs': '0', 'type': 'Link'}, 'model': {'native': False, 'name': 'model', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'volumeStorage': {'maxOccurs': 'unbounded', 'native': False, 'name': 'volumestorage', 'minOccurs': '0', 'type': 'Link'}, 'instanceId': {'native': True, 'name': 'instanceid', 'minOccurs': '0', 'type': 'string'}, 'state': {'native': False, 'name': 'state', 'minOccurs': '0', 'type': 'State'}, 'snapshots': {'maxOccurs': 'unbounded', 'native': False, 'name': 'snapshots', 'minOccurs': '0', 'type': 'Snapshot'}, 'startTime': {'native': True, 'name': 'starttime', 'minOccurs': '0', 'type': 'date'}, 'hostname': {'native': True, 'name': 'hostname', 'minOccurs': '0', 'type': 'string'}, 'publicAddress': {'native': True, 'name': 'publicaddress', 'minOccurs': '0', 'type': 'string'}, 'environment': {'native': False, 'name': 'environment', 'minOccurs': '0', 'type': 'Link'}, 'onboarded': {'native': True, 'name': 'onboarded', 'minOccurs': '0', 'type': 'boolean'}, 'createdOn': {'native': True, 'name': 'createdon', 'minOccurs': '0', 'type': 'date'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'stack': {'native': False, 'name': 'stack', 'minOccurs': '0', 'type': 'Link'}, 'image': {'native': False, 'name': 'image', 'minOccurs': '0', 'type': 'Link'}, 'lastStartedOrStoppedBy': {'native': True, 'name': 'laststartedorstoppedby', 'minOccurs': '0', 'type': 'string'}, 'lastUpdate': {'native': True, 'name': 'lastupdate', 'minOccurs': '0', 'type': 'date'}})
        self.scriptstatuslink = scriptstatuslink
        self.location = location
        self.resources = resources
        self.pending = pending
        self.canonicalname = canonicalname
        self.image = image
        self.createdon = createdon
        self.addresses = addresses
        self.privateaddress = privateaddress
        self.scriptstatus = scriptstatus
        self.variables = variables
        self.credential = credential
        self.template = template
        self.model = model
        self.properties = properties
        self.laststartedorstoppedby = laststartedorstoppedby
        self.instanceid = instanceid
        self.state = state
        self.snapshots = snapshots
        self.starttime = starttime
        self.lastupdate = lastupdate
        self.environment = environment
        self.onboarded = onboarded
        self.stoptime = stoptime
        self.cloud = cloud
        self.stack = stack
        self.hostname = hostname
        self.volumestorage = volumestorage
        self.publicaddress = publicaddress 
