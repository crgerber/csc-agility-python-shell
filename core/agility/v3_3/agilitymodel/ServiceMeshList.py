from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase
from core.agility.v3_3.agilitymodel.actions.ServiceMeshList import ServiceMeshListActions

class ServiceMeshList(ServiceMeshListBase, ServiceMeshListActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        ServiceMeshListBase.__init__(self)
