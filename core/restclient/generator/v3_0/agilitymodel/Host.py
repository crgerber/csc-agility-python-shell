from base.Host import HostBase
from actions.Host import HostActions

class Host(HostBase, HostActions):
    '''
    classdocs
    '''
    def __init__(self, credential=None, address=None):
        '''
        Constructor
        @param credential: credential minOccurs=0
        @type credential: Credential
        @param address: address minOccurs=0
        @type address: string
        '''
        HostBase.__init__(self, credential=credential, address=address)
