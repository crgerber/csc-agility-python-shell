from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class DesignItemBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, errorinfo=[], fixedordercont=None, anyordercont=None, layoutinfo=[], manualordercont=None, variable=[], dirty=False, manualorderposition=None, path=None, logicalid=None, fixedorderposition=None, layout=None, anyorderposition=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'logicalId': {'type': 'string', 'name': 'logicalid', 'minOccurs': '0', 'native': True}, 'fixedOrderCont': {'type': 'Link', 'name': 'fixedordercont', 'minOccurs': '0', 'native': False}, 'anyOrderCont': {'type': 'Link', 'name': 'anyordercont', 'minOccurs': '0', 'native': False}, 'layoutInfo': {'maxOccurs': 'unbounded', 'type': 'NameValuePair', 'name': 'layoutinfo', 'minOccurs': '0', 'native': False}, 'manualOrderCont': {'type': 'Link', 'name': 'manualordercont', 'minOccurs': '0', 'native': False}, 'anyOrderPosition': {'type': 'integer', 'name': 'anyorderposition', 'minOccurs': '0', 'native': True}, 'layout': {'type': 'string', 'name': 'layout', 'minOccurs': '0', 'native': True}, 'dirty': {'type': 'boolean', 'name': 'dirty', 'native': True}, 'variable': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'path': {'type': 'string', 'name': 'path', 'minOccurs': '0', 'native': True}, 'errorInfo': {'maxOccurs': 'unbounded', 'type': 'ErrorInfo', 'name': 'errorinfo', 'minOccurs': '0', 'native': False}, 'fixedOrderPosition': {'type': 'integer', 'name': 'fixedorderposition', 'minOccurs': '0', 'native': True}, 'manualOrderPosition': {'type': 'integer', 'name': 'manualorderposition', 'minOccurs': '0', 'native': True}})
        self.errorinfo = errorinfo
        self.fixedordercont = fixedordercont
        self.anyordercont = anyordercont
        self.layoutinfo = layoutinfo
        self.manualordercont = manualordercont
        self.variable = variable
        self.dirty = dirty
        self.manualorderposition = manualorderposition
        self.path = path
        self.logicalid = logicalid
        self.fixedorderposition = fixedorderposition
        self.layout = layout
        self.anyorderposition = anyorderposition 
