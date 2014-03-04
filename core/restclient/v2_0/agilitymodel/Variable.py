from core.restclient.v2_0.agilitymodel.base.Variable import VariableBase
from core.restclient.v2_0.agilitymodel.actions.Variable import VariableActions

class Variable(VariableBase, VariableActions):
    '''
    classdocs
    '''
    def __init__(self, value=None):
        '''
        Constructor
        @param value: value minOccurs=0
        @type value: string
        '''
        VariableBase.__init__(self, value=value)
