from core.restclient.v2_0.agilitymodel.base.Blueprint import BlueprintBase
from core.restclient.v2_0.agilitymodel.actions.Blueprint import BlueprintActions

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
