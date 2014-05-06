from core.agility.v3_0.agilitymodel.base.Link import LinkBase

class DescriptiveLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, description=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'minOccurs': '0', 'native': True}})
        self.displayname = displayname
        self.description = description 
