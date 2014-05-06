from core.agility.v2_0.agilitymodel.base.Command import CommandBase
from core.agility.v2_0.agilitymodel.actions.Command import CommandActions

class Command(CommandBase, CommandActions):
    '''
    classdocs
    '''
    def __init__(self, classname='', parameter=list(), name='', ignoreError=False):
        '''
        Constructor
        @param classname: classname
        @type classname: string
        @param parameter: parameter minOccurs=0 maxOccurs=unbounded
        @type parameter: Parameter
        @param name: name
        @type name: string
        @param ignoreError: ignoreError
        @type ignoreError: boolean
        '''
        CommandBase.__init__(self, classname=classname, parameter=parameter, name=name, ignoreError=ignoreError)
