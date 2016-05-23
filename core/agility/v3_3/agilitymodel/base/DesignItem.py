from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class DesignItemBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, anyorderposition=None, manualordercont=None, manualorderposition=None, dirty=False, variable=[], errorinfo=[], anyordercont=None, fixedordercont=None, layoutinfo=[], fixedorderposition=None, path=None, layout=None, logicalid=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'anyOrderPosition': {'name': 'anyorderposition', 'minOccurs': '0', 'native': True, 'type': 'integer'}, 'manualOrderCont': {'name': 'manualordercont', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'manualOrderPosition': {'name': 'manualorderposition', 'minOccurs': '0', 'native': True, 'type': 'integer'}, 'dirty': {'name': 'dirty', 'native': True, 'type': 'boolean'}, 'variable': {'name': 'variable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'logicalId': {'name': 'logicalid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'anyOrderCont': {'name': 'anyordercont', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'fixedOrderCont': {'name': 'fixedordercont', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'layoutInfo': {'name': 'layoutinfo', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'NameValuePair'}, 'fixedOrderPosition': {'name': 'fixedorderposition', 'minOccurs': '0', 'native': True, 'type': 'integer'}, 'path': {'name': 'path', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'layout': {'name': 'layout', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'errorInfo': {'name': 'errorinfo', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ErrorInfo'}})
        self.anyorderposition = anyorderposition
        self.manualordercont = manualordercont
        self.manualorderposition = manualorderposition
        self.dirty = dirty
        self.variable = variable
        self.errorinfo = errorinfo
        self.anyordercont = anyordercont
        self.fixedordercont = fixedordercont
        self.layoutinfo = layoutinfo
        self.fixedorderposition = fixedorderposition
        self.path = path
        self.layout = layout
        self.logicalid = logicalid 
