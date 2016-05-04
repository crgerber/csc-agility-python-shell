from base.Blueprint import BlueprintBase
from actions.Blueprint import BlueprintActions

class Blueprint(BlueprintBase, BlueprintActions):
    '''
    classdocs
    '''
    def __init__(self, connection=[], errorlevel=None, topology=[]):
        '''
        Constructor
        @param connection: connection minOccurs=0 maxOccurs=unbounded
        @type connection: DesignConnection
        @param errorlevel: errorlevel
        @type errorlevel: ErrorLevel
        @param topology: topology minOccurs=0 maxOccurs=unbounded
        @type topology: Link
        '''
        BlueprintBase.__init__(self, connection=connection, errorlevel=errorlevel, topology=topology)
