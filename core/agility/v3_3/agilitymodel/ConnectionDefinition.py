from core.agility.v3_3.agilitymodel.base.ConnectionDefinition import ConnectionDefinitionBase
from core.agility.v3_3.agilitymodel.actions.ConnectionDefinition import ConnectionDefinitionActions

class ConnectionDefinition(ConnectionDefinitionBase, ConnectionDefinitionActions):
    '''
    classdocs
    '''
    def __init__(self, sourcetype=None, displayname=None, destinationtype=None, connectiontype=None):
        '''
        Constructor
        @param sourcetype: sourcetype
        @type sourcetype: Link
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param destinationtype: destinationtype
        @type destinationtype: Link
        @param connectiontype: connectiontype
        @type connectiontype: Link
        '''
        ConnectionDefinitionBase.__init__(self, sourcetype=sourcetype, displayname=displayname, destinationtype=destinationtype, connectiontype=connectiontype)
