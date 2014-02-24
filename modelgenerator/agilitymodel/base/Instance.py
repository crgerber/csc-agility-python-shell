from Asset import AssetBase

class InstanceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, addresses=list(), lastUpdate=None, instanceId=None, variables=list(), snapshots=list(), cloud=None, publicAddress=None, hostname=None, stack=None, environment=None, state=None, stopTime=None, template=None, scriptstatus=list(), privateAddress=None, resources=list(), volumeStorage=list(), credential=list(), canonicalName=None, startTime=None, properties=list(), createdOn=None, onboarded=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'addresses': {'maxOccurs': 'unbounded', 'type': 'Address', 'name': 'addresses', 'minOccurs': '0', 'native': False}, 'credential': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'credential', 'minOccurs': '0', 'native': False}, 'instanceId': {'type': 'string', 'name': 'instanceId', 'minOccurs': '0', 'native': True}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'snapshots': {'maxOccurs': 'unbounded', 'type': 'Snapshot', 'name': 'snapshots', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'publicAddress': {'type': 'string', 'name': 'publicAddress', 'minOccurs': '0', 'native': True}, 'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'stack': {'type': 'Link', 'name': 'stack', 'minOccurs': '0', 'native': False}, 'environment': {'type': 'Link', 'name': 'environment', 'minOccurs': '0', 'native': False}, 'state': {'type': 'State', 'name': 'state', 'minOccurs': '0', 'native': False}, 'stopTime': {'type': 'date', 'name': 'stopTime', 'minOccurs': '0', 'native': True}, 'template': {'type': 'Link', 'name': 'template', 'minOccurs': '0', 'native': False}, 'scriptstatus': {'maxOccurs': 'unbounded', 'type': 'ScriptStatus', 'name': 'scriptstatus', 'minOccurs': '0', 'native': False}, 'privateAddress': {'type': 'string', 'name': 'privateAddress', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'volumeStorage': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'volumeStorage', 'minOccurs': '0', 'native': False}, 'lastUpdate': {'type': 'date', 'name': 'lastUpdate', 'minOccurs': '0', 'native': True}, 'canonicalName': {'type': 'string', 'name': 'canonicalName', 'minOccurs': '0', 'native': True}, 'startTime': {'type': 'date', 'name': 'startTime', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'createdOn': {'type': 'date', 'name': 'createdOn', 'minOccurs': '0', 'native': True}, 'onboarded': {'type': 'boolean', 'name': 'onboarded', 'minOccurs': '0', 'native': True}})
        self.addresses = addresses
        self.lastUpdate = lastUpdate
        self.instanceId = instanceId
        self.variables = variables
        self.snapshots = snapshots
        self.cloud = cloud
        self.publicAddress = publicAddress
        self.hostname = hostname
        self.stack = stack
        self.environment = environment
        self.state = state
        self.stopTime = stopTime
        self.template = template
        self.scriptstatus = scriptstatus
        self.privateAddress = privateAddress
        self.resources = resources
        self.volumeStorage = volumeStorage
        self.credential = credential
        self.canonicalName = canonicalName
        self.startTime = startTime
        self.properties = properties
        self.createdOn = createdOn
        self.onboarded = onboarded 
