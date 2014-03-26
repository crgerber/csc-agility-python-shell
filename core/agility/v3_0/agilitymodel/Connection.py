from core.agility.v3_0.agilitymodel.base.Connection import ConnectionBase
from core.agility.v3_0.agilitymodel.actions.Connection import ConnectionActions

class Connection(ConnectionBase, ConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, variable=[], source=None, destination=None):
        '''
        Constructor
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param source: source
        @type source: Link
        @param destination: destination
        @type destination: Link
        '''
        ConnectionBase.__init__(self, variable=variable, source=source, destination=destination)
