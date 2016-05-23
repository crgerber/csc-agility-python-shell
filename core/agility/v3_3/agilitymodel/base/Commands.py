from core.agility.common.AgilityModelBase import AgilityModelBase

class CommandsBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, productversion='', command=[], version=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'version': {'name': 'version', 'native': True, 'type': 'string'}, 'command': {'name': 'command', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Command'}, 'productVersion': {'name': 'productversion', 'native': True, 'type': 'string'}})
        self.productversion = productversion
        self.command = command
        self.version = version 
