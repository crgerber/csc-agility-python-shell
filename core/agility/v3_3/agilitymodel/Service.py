from core.agility.v3_3.agilitymodel.base.Service import ServiceBase
from core.agility.v3_3.agilitymodel.actions.Service import ServiceActions

class Service(ServiceBase, ServiceActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        ServiceBase.__init__(self)
