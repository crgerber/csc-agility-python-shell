from core.agility.v3_3.agilitymodel.base.Blueprint import BlueprintBase
from core.agility.v3_3.agilitymodel.actions.Blueprint import BlueprintActions

class Blueprint(BlueprintBase, BlueprintActions):
    '''
    classdocs
    '''
    def __init__(self, topology=[], errorlevel=None, connection=[]):
        '''
        Constructor
        @param topology: topology minOccurs=0 maxOccurs=unbounded
        @type topology: Link
        @param errorlevel: errorlevel
        @type errorlevel: ErrorLevel
        @param connection: connection minOccurs=0 maxOccurs=unbounded
        @type connection: DesignConnection
        '''
        BlueprintBase.__init__(self, topology=topology, errorlevel=errorlevel, connection=connection)
