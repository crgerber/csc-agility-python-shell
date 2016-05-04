from base.Parameter import ParameterBase
from actions.Parameter import ParameterActions

class Parameter(ParameterBase, ParameterActions):
    '''
    classdocs
    '''
    def __init__(self, name='', value=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param value: value
        @type value: string
        '''
        ParameterBase.__init__(self, name=name, value=value)
