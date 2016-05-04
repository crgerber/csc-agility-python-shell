from Asset import AssetBase

class DistNodeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, nodetype=None, nodestatus=None, hostname=None, state=None, version=None, packages=[], ipaddress=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'nodeType': {'type': 'string', 'name': 'nodetype', 'minOccurs': '0', 'native': True}, 'nodeStatus': {'type': 'string', 'name': 'nodestatus', 'minOccurs': '0', 'native': True}, 'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'state': {'type': 'State', 'name': 'state', 'minOccurs': '0', 'native': False}, 'version': {'type': 'string', 'name': 'version', 'minOccurs': '0', 'native': True}, 'packages': {'maxOccurs': 'unbounded', 'type': 'DistNodePackage', 'name': 'packages', 'minOccurs': '0', 'native': False}, 'ipAddress': {'type': 'string', 'name': 'ipaddress', 'minOccurs': '0', 'native': True}})
        self.nodetype = nodetype
        self.nodestatus = nodestatus
        self.hostname = hostname
        self.state = state
        self.version = version
        self.packages = packages
        self.ipaddress = ipaddress 
