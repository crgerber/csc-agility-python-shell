from core.agility.common.AgilityModelBase import AgilityModelBase

class AdapterInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, category='', symbolicname='', vendor='', name='', version='', dependencies=[], description=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'category': {'type': 'string', 'name': 'category', 'native': True}, 'symbolicName': {'type': 'string', 'name': 'symbolicname', 'native': True}, 'vendor': {'type': 'string', 'name': 'vendor', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'version': {'type': 'string', 'name': 'version', 'native': True}, 'dependencies': {'maxOccurs': 'unbounded', 'type': 'PackageInfo', 'name': 'dependencies', 'minOccurs': '0', 'native': False}, 'description': {'type': 'string', 'name': 'description', 'native': True}})
        self.category = category
        self.symbolicname = symbolicname
        self.vendor = vendor
        self.name = name
        self.version = version
        self.dependencies = dependencies
        self.description = description 
