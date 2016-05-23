from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class DistNodeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, state=None, nodetype=None, version=None, packages=[], ipaddress=None, hostname=None, nodestatus=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'state': {'name': 'state', 'minOccurs': '0', 'native': False, 'type': 'State'}, 'hostname': {'name': 'hostname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'nodeType': {'name': 'nodetype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'ipAddress': {'name': 'ipaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'packages': {'name': 'packages', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DistNodePackage'}, 'version': {'name': 'version', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'nodeStatus': {'name': 'nodestatus', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.state = state
        self.nodetype = nodetype
        self.version = version
        self.packages = packages
        self.ipaddress = ipaddress
        self.hostname = hostname
        self.nodestatus = nodestatus 
