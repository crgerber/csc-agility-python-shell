from core.agility.common.AgilityModelBase import AgilityModelBase

class AdapterInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, vendor='', description='', version='', name='', category='', dependencies=[], symbolicname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'name': 'description', 'native': True, 'type': 'string'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'version': {'name': 'version', 'native': True, 'type': 'string'}, 'vendor': {'name': 'vendor', 'native': True, 'type': 'string'}, 'symbolicName': {'name': 'symbolicname', 'native': True, 'type': 'string'}, 'category': {'name': 'category', 'native': True, 'type': 'string'}, 'dependencies': {'name': 'dependencies', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PackageInfo'}})
        self.vendor = vendor
        self.description = description
        self.version = version
        self.name = name
        self.category = category
        self.dependencies = dependencies
        self.symbolicname = symbolicname 
