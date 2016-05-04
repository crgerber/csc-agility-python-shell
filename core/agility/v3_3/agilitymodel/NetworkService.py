from base.NetworkService import NetworkServiceBase
from actions.NetworkService import NetworkServiceActions

class NetworkService(NetworkServiceBase, NetworkServiceActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        NetworkServiceBase.__init__(self)
