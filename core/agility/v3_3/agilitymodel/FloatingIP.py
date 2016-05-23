from core.agility.v3_3.agilitymodel.base.FloatingIP import FloatingIPBase
from core.agility.v3_3.agilitymodel.actions.FloatingIP import FloatingIPActions

class FloatingIP(FloatingIPBase, FloatingIPActions):
    '''
    classdocs
    '''
    def __init__(self, floatingipaddress=None, floatingnetwork=None, tenantid=None, port=None, floatingipid=None, fixedipaddress=None, networkprovider=None):
        '''
        Constructor
        @param floatingipaddress: floatingipaddress minOccurs=0
        @type floatingipaddress: string
        @param floatingnetwork: floatingnetwork minOccurs=0
        @type floatingnetwork: Link
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param port: port minOccurs=0
        @type port: Link
        @param floatingipid: floatingipid minOccurs=0
        @type floatingipid: string
        @param fixedipaddress: fixedipaddress minOccurs=0
        @type fixedipaddress: string
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        '''
        FloatingIPBase.__init__(self, floatingipaddress=floatingipaddress, floatingnetwork=floatingnetwork, tenantid=tenantid, port=port, floatingipid=floatingipid, fixedipaddress=fixedipaddress, networkprovider=networkprovider)
