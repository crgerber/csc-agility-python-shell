from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ConnectionDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, destinationtype=None, connectiontype=None, displayname=None, sourcetype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'destinationType': {'name': 'destinationtype', 'native': False, 'type': 'Link'}, 'connectionType': {'name': 'connectiontype', 'native': False, 'type': 'Link'}, 'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'sourceType': {'name': 'sourcetype', 'native': False, 'type': 'Link'}})
        self.destinationtype = destinationtype
        self.connectiontype = connectiontype
        self.displayname = displayname
        self.sourcetype = sourcetype 
