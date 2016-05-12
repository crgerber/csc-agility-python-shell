from core.agility.v3_3.agilitymodel.base.Blueprint import BlueprintBase
from core.agility.v3_3.agilitymodel.actions.Blueprint import BlueprintActions

class Blueprint(BlueprintBase, BlueprintActions):
    '''
    classdocs
    '''
    def __init__(self, errorlevel=None, topology=[], connection=[]):
        '''
        Constructor
        @param errorlevel: errorlevel
        @type errorlevel: ErrorLevel
        @param topology: topology minOccurs=0 maxOccurs=unbounded
        @type topology: Link
        @param connection: connection minOccurs=0 maxOccurs=unbounded
        @type connection: DesignConnection
        '''
        BlueprintBase.__init__(self, errorlevel=errorlevel, topology=topology, connection=connection)