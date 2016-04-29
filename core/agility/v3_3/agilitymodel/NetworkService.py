from core.agility.v3_3.agilitymodel.base.NetworkService import NetworkServiceBase
from core.agility.v3_3.agilitymodel.actions.NetworkService import NetworkServiceActions

class NetworkService(NetworkServiceBase, NetworkServiceActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        NetworkServiceBase.__init__(self)
