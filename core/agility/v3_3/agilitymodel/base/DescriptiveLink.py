from core.agility.v3_3.agilitymodel.base.Link import LinkBase

class DescriptiveLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, description=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'description': {'native': True, 'name': 'description', 'minOccurs': '0', 'type': 'string'}})
        self.displayname = displayname
        self.description = description 
