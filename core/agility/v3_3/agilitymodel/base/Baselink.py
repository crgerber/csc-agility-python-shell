from core.agility.common.AgilityModelBase import AgilityModelBase

class BaselinkBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name=None, href=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'href': {'name': 'href', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.name = name
        self.href = href 
