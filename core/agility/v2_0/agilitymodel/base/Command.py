from core.agility.common.AgilityModelBase import AgilityModelBase


class CommandBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, classname='', parameter=list(), name='', ignoreError=False):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'classname': {'use': 'required', 'type': 'string', 'name': 'classname', 'native': True}, 'parameter': {'maxOccurs': 'unbounded', 'type': 'Parameter', 'name': 'parameter', 'minOccurs': '0', 'native': False}, 'name': {'use': 'required', 'type': 'string', 'name': 'name', 'native': True}, 'ignoreError': {'default': 'false', 'type': 'boolean', 'name': 'ignoreError', 'native': True}})
        self.classname = classname
        self.parameter = parameter
        self.name = name
        self.ignoreError = ignoreError 
