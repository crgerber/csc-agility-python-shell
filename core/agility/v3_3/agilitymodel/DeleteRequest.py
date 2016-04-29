from core.agility.v3_3.agilitymodel.base.DeleteRequest import DeleteRequestBase
from core.agility.v3_3.agilitymodel.actions.DeleteRequest import DeleteRequestActions

class DeleteRequest(DeleteRequestBase, DeleteRequestActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        DeleteRequestBase.__init__(self)
