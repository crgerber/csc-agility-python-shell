from base.Commands import CommandsBase
from actions.Commands import CommandsActions

class Commands(CommandsBase, CommandsActions):
    '''
    classdocs
    '''
    def __init__(self, version='', command=[], productversion=''):
        '''
        Constructor
        @param version: version
        @type version: string
        @param command: command minOccurs=0 maxOccurs=unbounded
        @type command: Command
        @param productversion: productversion
        @type productversion: string
        '''
        CommandsBase.__init__(self, version=version, command=command, productversion=productversion)
