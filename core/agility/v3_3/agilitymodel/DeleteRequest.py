from base.DeleteRequest import DeleteRequestBase
from actions.DeleteRequest import DeleteRequestActions

class DeleteRequest(DeleteRequestBase, DeleteRequestActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        DeleteRequestBase.__init__(self)
