from core.agility.common.AgilityModelBase import AgilityModelBase

class CommandsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, command=[], version='', productversion=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'command': {'maxOccurs': 'unbounded', 'native': False, 'name': 'command', 'minOccurs': '0', 'type': 'Command'}, 'version': {'native': True, 'name': 'version', 'type': 'string'}, 'productVersion': {'native': True, 'name': 'productversion', 'type': 'string'}})
        self.command = command
        self.version = version
        self.productversion = productversion 
