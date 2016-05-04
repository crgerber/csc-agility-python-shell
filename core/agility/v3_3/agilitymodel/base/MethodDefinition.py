from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class MethodDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, parameter=[], displayname=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'parameter': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'parameter', 'minOccurs': '0', 'native': False}})
        self.parameter = parameter
        self.displayname = displayname 
