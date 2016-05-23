from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class MethodDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, parameter=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'parameter': {'name': 'parameter', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyDefinition'}})
        self.displayname = displayname
        self.parameter = parameter 
