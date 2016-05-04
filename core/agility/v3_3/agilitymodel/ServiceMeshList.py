from base.ServiceMeshList import ServiceMeshListBase
from actions.ServiceMeshList import ServiceMeshListActions

class ServiceMeshList(ServiceMeshListBase, ServiceMeshListActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        ServiceMeshListBase.__init__(self)
