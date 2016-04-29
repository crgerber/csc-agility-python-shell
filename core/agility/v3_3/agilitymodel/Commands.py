from core.agility.v3_3.agilitymodel.base.Commands import CommandsBase
from core.agility.v3_3.agilitymodel.actions.Commands import CommandsActions

class Commands(CommandsBase, CommandsActions):
    '''
    classdocs
    '''
    def __init__(self, command=[], version='', productversion=''):
        '''
        Constructor
        @param command: command minOccurs=0 maxOccurs=unbounded
        @type command: Command
        @param version: version
        @type version: string
        @param productversion: productversion
        @type productversion: string
        '''
        CommandsBase.__init__(self, command=command, version=version, productversion=productversion)
