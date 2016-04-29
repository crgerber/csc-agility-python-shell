from core.agility.common.AgilityModelBase import AgilityModelBase

class ScriptUsageBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, category=None, script=None, package=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'category': {'native': True, 'name': 'category', 'minOccurs': '0', 'type': 'string'}, 'script': {'native': False, 'name': 'script', 'minOccurs': '0', 'type': 'Script'}, 'package': {'native': False, 'name': 'package', 'minOccurs': '0', 'type': 'Package'}})
        self.category = category
        self.script = script
        self.package = package 
