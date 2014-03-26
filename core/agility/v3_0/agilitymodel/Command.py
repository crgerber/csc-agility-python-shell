from core.agility.v3_0.agilitymodel.base.Command import CommandBase
from core.agility.v3_0.agilitymodel.actions.Command import CommandActions

class Command(CommandBase, CommandActions):
    '''
    classdocs
    '''
    def __init__(self, classname='', parameter=[], name='', ignoreerror=False):
        '''
        Constructor
        @param classname: classname
        @type classname: string
        @param parameter: parameter minOccurs=0 maxOccurs=unbounded
        @type parameter: Parameter
        @param name: name
        @type name: string
        @param ignoreerror: ignoreerror
        @type ignoreerror: boolean
        '''
        CommandBase.__init__(self, classname=classname, parameter=parameter, name=name, ignoreerror=ignoreerror)
