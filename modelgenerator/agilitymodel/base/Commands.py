from AgilityModelBase import AgilityModelBase

class CommandsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, version='', command=list(), productVersion=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'version': {'type': 'string', 'name': 'version', 'native': True}, 'command': {'maxOccurs': 'unbounded', 'type': 'Command', 'name': 'command', 'minOccurs': '0', 'native': False}, 'productVersion': {'type': 'string', 'name': 'productVersion', 'native': True}})
        self.version = version
        self.command = command
        self.productVersion = productVersion 
