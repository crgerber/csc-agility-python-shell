from core.agility.v3_3.agilitymodel.base.Connection import ConnectionBase
from core.agility.v3_3.agilitymodel.actions.Connection import ConnectionActions

class Connection(ConnectionBase, ConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, destination=None, source=None, variable=[]):
        '''
        Constructor
        @param destination: destination
        @type destination: Link
        @param source: source
        @type source: Link
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        '''
        ConnectionBase.__init__(self, destination=destination, source=source, variable=variable)
