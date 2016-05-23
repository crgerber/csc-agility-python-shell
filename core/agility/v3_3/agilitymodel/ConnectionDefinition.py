from core.agility.v3_3.agilitymodel.base.ConnectionDefinition import ConnectionDefinitionBase
from core.agility.v3_3.agilitymodel.actions.ConnectionDefinition import ConnectionDefinitionActions

class ConnectionDefinition(ConnectionDefinitionBase, ConnectionDefinitionActions):
    '''
    classdocs
    '''
    def __init__(self, destinationtype=None, connectiontype=None, displayname=None, sourcetype=None):
        '''
        Constructor
        @param destinationtype: destinationtype
        @type destinationtype: Link
        @param connectiontype: connectiontype
        @type connectiontype: Link
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param sourcetype: sourcetype
        @type sourcetype: Link
        '''
        ConnectionDefinitionBase.__init__(self, destinationtype=destinationtype, connectiontype=connectiontype, displayname=displayname, sourcetype=sourcetype)
