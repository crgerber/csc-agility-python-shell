from core.agility.v3_3.agilitymodel.base.FloatingIP import FloatingIPBase
from core.agility.v3_3.agilitymodel.actions.FloatingIP import FloatingIPActions

class FloatingIP(FloatingIPBase, FloatingIPActions):
    '''
    classdocs
    '''
    def __init__(self, floatingipaddress=None, tenantid=None, networkprovider=None, port=None, floatingipid=None, fixedipaddress=None, floatingnetwork=None):
        '''
        Constructor
        @param floatingipaddress: floatingipaddress minOccurs=0
        @type floatingipaddress: string
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        @param port: port minOccurs=0
        @type port: Link
        @param floatingipid: floatingipid minOccurs=0
        @type floatingipid: string
        @param fixedipaddress: fixedipaddress minOccurs=0
        @type fixedipaddress: string
        @param floatingnetwork: floatingnetwork minOccurs=0
        @type floatingnetwork: Link
        '''
        FloatingIPBase.__init__(self, floatingipaddress=floatingipaddress, tenantid=tenantid, networkprovider=networkprovider, port=port, floatingipid=floatingipid, fixedipaddress=fixedipaddress, floatingnetwork=floatingnetwork)
