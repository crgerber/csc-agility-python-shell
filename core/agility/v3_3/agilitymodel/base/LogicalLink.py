from core.agility.v3_3.agilitymodel.base.Link import LinkBase

class LogicalLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, logicalid=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'logicalId': {'native': True, 'name': 'logicalid', 'minOccurs': '0', 'type': 'string'}})
        self.logicalid = logicalid 
