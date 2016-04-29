from core.agility.common.AgilityModelBase import AgilityModelBase

class BaselinkBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name=None, href=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'href': {'native': True, 'name': 'href', 'minOccurs': '0', 'type': 'string'}})
        self.name = name
        self.href = href 
