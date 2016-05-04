from Asset import AssetBase

class InstanceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, addresses=[], lastupdate=None, instanceid=None, variables=[], snapshots=[], cloud=None, publicaddress=None, image=None, hostname=None, laststartedorstoppedby=None, stack=None, environment=None, state=None, stoptime=None, location=None, template=None, scriptstatus=[], privateaddress=None, resources=[], volumestorage=[], credential=[], canonicalname=None, scriptstatuslink=[], starttime=None, properties=[], createdon=None, pending=None, model=None, onboarded=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'addresses': {'maxOccurs': 'unbounded', 'type': 'Address', 'name': 'addresses', 'minOccurs': '0', 'native': False}, 'credential': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'credential', 'minOccurs': '0', 'native': False}, 'instanceId': {'type': 'string', 'name': 'instanceid', 'minOccurs': '0', 'native': True}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'snapshots': {'maxOccurs': 'unbounded', 'type': 'Snapshot', 'name': 'snapshots', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'publicAddress': {'type': 'string', 'name': 'publicaddress', 'minOccurs': '0', 'native': True}, 'image': {'type': 'Link', 'name': 'image', 'minOccurs': '0', 'native': False}, 'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'lastStartedOrStoppedBy': {'type': 'string', 'name': 'laststartedorstoppedby', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'environment': {'type': 'Link', 'name': 'environment', 'minOccurs': '0', 'native': False}, 'state': {'type': 'State', 'name': 'state', 'minOccurs': '0', 'native': False}, 'stopTime': {'type': 'date', 'name': 'stoptime', 'minOccurs': '0', 'native': True}, 'location': {'type': 'Link', 'name': 'location', 'minOccurs': '0', 'native': False}, 'template': {'type': 'Link', 'name': 'template', 'minOccurs': '0', 'native': False}, 'scriptstatus': {'maxOccurs': 'unbounded', 'type': 'ScriptStatus', 'name': 'scriptstatus', 'minOccurs': '0', 'native': False}, 'privateAddress': {'type': 'string', 'name': 'privateaddress', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'volumeStorage': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'volumestorage', 'minOccurs': '0', 'native': False}, 'lastUpdate': {'type': 'date', 'name': 'lastupdate', 'minOccurs': '0', 'native': True}, 'canonicalName': {'type': 'string', 'name': 'canonicalname', 'minOccurs': '0', 'native': True}, 'scriptstatusLink': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'scriptstatuslink', 'minOccurs': '0', 'native': False}, 'startTime': {'type': 'date', 'name': 'starttime', 'minOccurs': '0', 'native': True}, 'stack': {'type': 'Link', 'name': 'stack', 'minOccurs': '0', 'native': False}, 'createdOn': {'type': 'date', 'name': 'createdon', 'minOccurs': '0', 'native': True}, 'pending': {'type': 'boolean', 'name': 'pending', 'minOccurs': '0', 'native': True}, 'model': {'type': 'Link', 'name': 'model', 'minOccurs': '0', 'native': False}, 'onboarded': {'type': 'boolean', 'name': 'onboarded', 'minOccurs': '0', 'native': True}})
        self.addresses = addresses
        self.lastupdate = lastupdate
        self.instanceid = instanceid
        self.variables = variables
        self.snapshots = snapshots
        self.cloud = cloud
        self.publicaddress = publicaddress
        self.image = image
        self.hostname = hostname
        self.laststartedorstoppedby = laststartedorstoppedby
        self.stack = stack
        self.environment = environment
        self.state = state
        self.stoptime = stoptime
        self.location = location
        self.template = template
        self.scriptstatus = scriptstatus
        self.privateaddress = privateaddress
        self.resources = resources
        self.volumestorage = volumestorage
        self.credential = credential
        self.canonicalname = canonicalname
        self.scriptstatuslink = scriptstatuslink
        self.starttime = starttime
        self.properties = properties
        self.createdon = createdon
        self.pending = pending
        self.model = model
        self.onboarded = onboarded 
