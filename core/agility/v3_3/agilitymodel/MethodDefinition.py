from core.agility.v3_3.agilitymodel.base.MethodDefinition import MethodDefinitionBase
from core.agility.v3_3.agilitymodel.actions.MethodDefinition import MethodDefinitionActions

class MethodDefinition(MethodDefinitionBase, MethodDefinitionActions):
    '''
    classdocs
    '''
    def __init__(self, parameter=[], displayname=None):
        '''
        Constructor
        @param parameter: parameter minOccurs=0 maxOccurs=unbounded
        @type parameter: PropertyDefinition
        @param displayname: displayname minOccurs=0
        @type displayname: string
        '''
        MethodDefinitionBase.__init__(self, parameter=parameter, displayname=displayname)
