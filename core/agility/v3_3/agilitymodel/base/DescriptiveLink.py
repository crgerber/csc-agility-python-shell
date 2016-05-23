from core.agility.v3_3.agilitymodel.base.Link import LinkBase

class DescriptiveLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, description=None, displayname=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'name': 'description', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.description = description
        self.displayname = displayname 
