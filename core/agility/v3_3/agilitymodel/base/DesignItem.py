from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class DesignItemBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, layoutinfo=[], errorinfo=[], path=None, dirty=False, anyorderposition=None, anyordercont=None, fixedordercont=None, fixedorderposition=None, layout=None, manualorderposition=None, manualordercont=None, logicalid=None, variable=[]):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'layoutInfo': {'maxOccurs': 'unbounded', 'native': False, 'name': 'layoutinfo', 'minOccurs': '0', 'type': 'NameValuePair'}, 'errorInfo': {'maxOccurs': 'unbounded', 'native': False, 'name': 'errorinfo', 'minOccurs': '0', 'type': 'ErrorInfo'}, 'path': {'native': True, 'name': 'path', 'minOccurs': '0', 'type': 'string'}, 'dirty': {'native': True, 'name': 'dirty', 'type': 'boolean'}, 'anyOrderPosition': {'native': True, 'name': 'anyorderposition', 'minOccurs': '0', 'type': 'integer'}, 'anyOrderCont': {'native': False, 'name': 'anyordercont', 'minOccurs': '0', 'type': 'Link'}, 'fixedOrderCont': {'native': False, 'name': 'fixedordercont', 'minOccurs': '0', 'type': 'Link'}, 'fixedOrderPosition': {'native': True, 'name': 'fixedorderposition', 'minOccurs': '0', 'type': 'integer'}, 'layout': {'native': True, 'name': 'layout', 'minOccurs': '0', 'type': 'string'}, 'manualOrderPosition': {'native': True, 'name': 'manualorderposition', 'minOccurs': '0', 'type': 'integer'}, 'manualOrderCont': {'native': False, 'name': 'manualordercont', 'minOccurs': '0', 'type': 'Link'}, 'logicalId': {'native': True, 'name': 'logicalid', 'minOccurs': '0', 'type': 'string'}, 'variable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variable', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.layoutinfo = layoutinfo
        self.errorinfo = errorinfo
        self.path = path
        self.dirty = dirty
        self.anyorderposition = anyorderposition
        self.anyordercont = anyordercont
        self.fixedordercont = fixedordercont
        self.fixedorderposition = fixedorderposition
        self.layout = layout
        self.manualorderposition = manualorderposition
        self.manualordercont = manualordercont
        self.logicalid = logicalid
        self.variable = variable 
