from core.agility.v3_3.agilitymodel.base.Connection import ConnectionBase
from core.agility.v3_3.agilitymodel.actions.Connection import ConnectionActions

class Connection(ConnectionBase, ConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, destination=None, variable=[], source=None):
        '''
        Constructor
        @param destination: destination
        @type destination: Link
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param source: source
        @type source: Link
        '''
        ConnectionBase.__init__(self, destination=destination, variable=variable, source=source)
