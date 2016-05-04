from core.agility.common.AgilityModelBase import AgilityModelBase

class ScriptUsageBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, category=None, package=None, script=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'category': {'type': 'string', 'name': 'category', 'minOccurs': '0', 'native': True}, 'script': {'type': 'Script', 'name': 'script', 'minOccurs': '0', 'native': False}, 'package': {'type': 'Package', 'name': 'package', 'minOccurs': '0', 'native': False}})
        self.category = category
        self.package = package
        self.script = script 
