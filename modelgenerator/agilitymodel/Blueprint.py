from base.Blueprint import BlueprintBase
from actions.Blueprint import BlueprintActions

class Blueprint(BlueprintBase, BlueprintActions):
    '''
    classdocs
    '''
    def __init__(self, connection=list(), errorLevel=None, topology=list()):
        '''
        Constructor
        @param connection: connection minOccurs=0 maxOccurs=unbounded
        @type connection: DesignConnection
        @param errorLevel: errorLevel
        @type errorLevel: ErrorLevel
        @param topology: topology minOccurs=0 maxOccurs=unbounded
        @type topology: Link
        '''
        BlueprintBase.__init__(self, connection=connection, errorLevel=errorLevel, topology=topology)
