from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ConnectionDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, sourcetype=None, displayname=None, destinationtype=None, connectiontype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'sourceType': {'native': False, 'name': 'sourcetype', 'type': 'Link'}, 'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'connectionType': {'native': False, 'name': 'connectiontype', 'type': 'Link'}, 'destinationType': {'native': False, 'name': 'destinationtype', 'type': 'Link'}})
        self.sourcetype = sourcetype
        self.displayname = displayname
        self.destinationtype = destinationtype
        self.connectiontype = connectiontype 
