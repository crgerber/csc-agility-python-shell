from DesignItem import DesignItemBase

class DesignConnectionBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, srcLogicalId=None, destLogicalId=None, srcId=None, destId=None):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'srcLogicalId': {'type': 'string', 'name': 'srcLogicalId', 'minOccurs': '0', 'native': True}, 'destLogicalId': {'type': 'string', 'name': 'destLogicalId', 'minOccurs': '0', 'native': True}, 'srcId': {'type': 'int', 'name': 'srcId', 'minOccurs': '0', 'native': True}, 'destId': {'type': 'int', 'name': 'destId', 'minOccurs': '0', 'native': True}})
        self.srcLogicalId = srcLogicalId
        self.destLogicalId = destLogicalId
        self.srcId = srcId
        self.destId = destId 
