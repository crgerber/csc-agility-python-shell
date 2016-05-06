from core.agility.v3_3.agilitymodel.base.InstanceVariableResponse import InstanceVariableResponseBase
from core.agility.v3_3.agilitymodel.actions.InstanceVariableResponse import InstanceVariableResponseActions

class InstanceVariableResponse(InstanceVariableResponseBase, InstanceVariableResponseActions):
    '''
    classdocs
    '''
    def __init__(self, variables=[]):
        '''
        Constructor
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: Variable
        '''
        InstanceVariableResponseBase.__init__(self, variables=variables)
