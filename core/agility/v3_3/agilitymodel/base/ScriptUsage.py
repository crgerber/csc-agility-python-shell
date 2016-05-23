from core.agility.common.AgilityModelBase import AgilityModelBase

class ScriptUsageBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, script=None, package=None, category=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'script': {'name': 'script', 'minOccurs': '0', 'native': False, 'type': 'Script'}, 'package': {'name': 'package', 'minOccurs': '0', 'native': False, 'type': 'Package'}, 'category': {'name': 'category', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.script = script
        self.package = package
        self.category = category 
