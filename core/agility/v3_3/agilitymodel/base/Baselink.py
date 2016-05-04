from core.agility.common.AgilityModelBase import AgilityModelBase

class BaselinkBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, href=None, name=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'href': {'type': 'string', 'name': 'href', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}})
        self.href = href
        self.name = name 
