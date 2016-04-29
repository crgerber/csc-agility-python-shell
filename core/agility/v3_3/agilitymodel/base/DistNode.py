from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class DistNodeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, ipaddress=None, version=None, nodestatus=None, packages=[], nodetype=None, state=None, hostname=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'nodeStatus': {'native': True, 'name': 'nodestatus', 'minOccurs': '0', 'type': 'string'}, 'nodeType': {'native': True, 'name': 'nodetype', 'minOccurs': '0', 'type': 'string'}, 'ipAddress': {'native': True, 'name': 'ipaddress', 'minOccurs': '0', 'type': 'string'}, 'packages': {'maxOccurs': 'unbounded', 'native': False, 'name': 'packages', 'minOccurs': '0', 'type': 'DistNodePackage'}, 'version': {'native': True, 'name': 'version', 'minOccurs': '0', 'type': 'string'}, 'state': {'native': False, 'name': 'state', 'minOccurs': '0', 'type': 'State'}, 'hostname': {'native': True, 'name': 'hostname', 'minOccurs': '0', 'type': 'string'}})
        self.ipaddress = ipaddress
        self.version = version
        self.nodestatus = nodestatus
        self.packages = packages
        self.nodetype = nodetype
        self.state = state
        self.hostname = hostname 
