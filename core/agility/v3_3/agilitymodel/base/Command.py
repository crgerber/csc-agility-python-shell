from core.agility.common.AgilityModelBase import AgilityModelBase

class CommandBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', ignoreerror=False, parameter=[], classname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'parameter': {'maxOccurs': 'unbounded', 'native': False, 'name': 'parameter', 'minOccurs': '0', 'type': 'Parameter'}, 'ignoreError': {'default': 'false', 'native': True, 'name': 'ignoreerror', 'type': 'boolean'}, 'name': {'native': True, 'name': 'name', 'use': 'required', 'type': 'string'}, 'classname': {'native': True, 'name': 'classname', 'use': 'required', 'type': 'string'}})
        self.name = name
        self.ignoreerror = ignoreerror
        self.parameter = parameter
        self.classname = classname 
