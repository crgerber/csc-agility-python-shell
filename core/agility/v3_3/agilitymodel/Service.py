from base.Service import ServiceBase
from actions.Service import ServiceActions

class Service(ServiceBase, ServiceActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        ServiceBase.__init__(self)
