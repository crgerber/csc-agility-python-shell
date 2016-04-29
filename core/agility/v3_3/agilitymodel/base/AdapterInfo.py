from core.agility.common.AgilityModelBase import AgilityModelBase

class AdapterInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, category='', dependencies=[], version='', description='', symbolicname='', vendor='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'category': {'native': True, 'name': 'category', 'type': 'string'}, 'dependencies': {'maxOccurs': 'unbounded', 'native': False, 'name': 'dependencies', 'minOccurs': '0', 'type': 'PackageInfo'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}, 'symbolicName': {'native': True, 'name': 'symbolicname', 'type': 'string'}, 'vendor': {'native': True, 'name': 'vendor', 'type': 'string'}, 'version': {'native': True, 'name': 'version', 'type': 'string'}})
        self.category = category
        self.dependencies = dependencies
        self.version = version
        self.description = description
        self.symbolicname = symbolicname
        self.vendor = vendor
        self.name = name 
