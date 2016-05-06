from core.agility.v3_3.agilitymodel.base.ConnectionDefinition import ConnectionDefinitionBase
from core.agility.v3_3.agilitymodel.actions.ConnectionDefinition import ConnectionDefinitionActions

class ConnectionDefinition(ConnectionDefinitionBase, ConnectionDefinitionActions):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, sourcetype=None, connectiontype=None, destinationtype=None):
        '''
        Constructor
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param sourcetype: sourcetype
        @type sourcetype: Link
        @param connectiontype: connectiontype
        @type connectiontype: Link
        @param destinationtype: destinationtype
        @type destinationtype: Link
        '''
        ConnectionDefinitionBase.__init__(self, displayname=displayname, sourcetype=sourcetype, connectiontype=connectiontype, destinationtype=destinationtype)
