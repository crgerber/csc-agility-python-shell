from VersionedItem import VersionedItemBase

class DesignItemBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, errorInfo=list(), fixedOrderCont=None, anyOrderCont=None, layoutInfo=list(), manualOrderCont=None, variable=list(), dirty=False, manualOrderPosition=None, path=None, logicalId=None, fixedOrderPosition=None, layout=None, anyOrderPosition=None):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'logicalId': {'type': 'string', 'name': 'logicalId', 'minOccurs': '0', 'native': True}, 'fixedOrderCont': {'type': 'Link', 'name': 'fixedOrderCont', 'minOccurs': '0', 'native': False}, 'anyOrderCont': {'type': 'Link', 'name': 'anyOrderCont', 'minOccurs': '0', 'native': False}, 'layoutInfo': {'maxOccurs': 'unbounded', 'type': 'NameValuePair', 'name': 'layoutInfo', 'minOccurs': '0', 'native': False}, 'manualOrderCont': {'type': 'Link', 'name': 'manualOrderCont', 'minOccurs': '0', 'native': False}, 'anyOrderPosition': {'type': 'integer', 'name': 'anyOrderPosition', 'minOccurs': '0', 'native': True}, 'layout': {'type': 'string', 'name': 'layout', 'minOccurs': '0', 'native': True}, 'dirty': {'type': 'boolean', 'name': 'dirty', 'native': True}, 'variable': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'path': {'type': 'string', 'name': 'path', 'minOccurs': '0', 'native': True}, 'errorInfo': {'maxOccurs': 'unbounded', 'type': 'ErrorInfo', 'name': 'errorInfo', 'minOccurs': '0', 'native': False}, 'fixedOrderPosition': {'type': 'integer', 'name': 'fixedOrderPosition', 'minOccurs': '0', 'native': True}, 'manualOrderPosition': {'type': 'integer', 'name': 'manualOrderPosition', 'minOccurs': '0', 'native': True}})
        self.errorInfo = errorInfo
        self.fixedOrderCont = fixedOrderCont
        self.anyOrderCont = anyOrderCont
        self.layoutInfo = layoutInfo
        self.manualOrderCont = manualOrderCont
        self.variable = variable
        self.dirty = dirty
        self.manualOrderPosition = manualOrderPosition
        self.path = path
        self.logicalId = logicalId
        self.fixedOrderPosition = fixedOrderPosition
        self.layout = layout
        self.anyOrderPosition = anyOrderPosition 
