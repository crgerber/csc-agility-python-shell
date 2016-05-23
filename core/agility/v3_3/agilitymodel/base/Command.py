from core.agility.common.AgilityModelBase import AgilityModelBase

class CommandBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', ignoreerror=False, classname='', parameter=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string', 'use': 'required'}, 'parameter': {'name': 'parameter', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Parameter'}, 'classname': {'name': 'classname', 'native': True, 'type': 'string', 'use': 'required'}, 'ignoreError': {'name': 'ignoreerror', 'default': 'false', 'native': True, 'type': 'boolean'}})
        self.name = name
        self.ignoreerror = ignoreerror
        self.classname = classname
        self.parameter = parameter 
