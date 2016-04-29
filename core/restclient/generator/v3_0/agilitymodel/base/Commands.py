from .AgilityModelBase import AgilityModelBase

class CommandsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, version='', command=[], productversion=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'version': {'type': 'string', 'name': 'version', 'native': True}, 'command': {'maxOccurs': 'unbounded', 'type': 'Command', 'name': 'command', 'minOccurs': '0', 'native': False}, 'productVersion': {'type': 'string', 'name': 'productversion', 'native': True}})
        self.version = version
        self.command = command
        self.productversion = productversion 
