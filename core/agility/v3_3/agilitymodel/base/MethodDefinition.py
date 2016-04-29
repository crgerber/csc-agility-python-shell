from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class MethodDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, parameter=[], displayname=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'parameter': {'maxOccurs': 'unbounded', 'native': False, 'name': 'parameter', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}})
        self.parameter = parameter
        self.displayname = displayname 
