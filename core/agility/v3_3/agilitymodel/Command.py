from core.agility.v3_3.agilitymodel.base.Command import CommandBase
from core.agility.v3_3.agilitymodel.actions.Command import CommandActions

class Command(CommandBase, CommandActions):
    '''
    classdocs
    '''
    def __init__(self, name='', ignoreerror=False, parameter=[], classname=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param ignoreerror: ignoreerror
        @type ignoreerror: boolean
        @param parameter: parameter minOccurs=0 maxOccurs=unbounded
        @type parameter: Parameter
        @param classname: classname
        @type classname: string
        '''
        CommandBase.__init__(self, name=name, ignoreerror=ignoreerror, parameter=parameter, classname=classname)
