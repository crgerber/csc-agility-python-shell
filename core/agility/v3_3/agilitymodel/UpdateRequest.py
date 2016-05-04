from base.UpdateRequest import UpdateRequestBase
from actions.UpdateRequest import UpdateRequestActions

class UpdateRequest(UpdateRequestBase, UpdateRequestActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        UpdateRequestBase.__init__(self)
