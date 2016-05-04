from Asset import AssetBase

class ConnectionDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, sourcetype=None, connectiontype=None, destinationtype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'sourceType': {'type': 'Link', 'name': 'sourcetype', 'native': False}, 'connectionType': {'type': 'Link', 'name': 'connectiontype', 'native': False}, 'destinationType': {'type': 'Link', 'name': 'destinationtype', 'native': False}})
        self.displayname = displayname
        self.sourcetype = sourcetype
        self.connectiontype = connectiontype
        self.destinationtype = destinationtype 
