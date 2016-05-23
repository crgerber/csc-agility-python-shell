from core.agility.v3_3.agilitymodel.base.Host import HostBase
from core.agility.v3_3.agilitymodel.actions.Host import HostActions

class Host(HostBase, HostActions):
    '''
    classdocs
    '''
    def __init__(self, address=None, credential=None):
        '''
        Constructor
        @param address: address minOccurs=0
        @type address: string
        @param credential: credential minOccurs=0
        @type credential: Credential
        '''
        HostBase.__init__(self, address=address, credential=credential)
