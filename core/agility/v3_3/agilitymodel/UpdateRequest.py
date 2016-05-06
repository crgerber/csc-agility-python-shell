from core.agility.v3_3.agilitymodel.base.UpdateRequest import UpdateRequestBase
from core.agility.v3_3.agilitymodel.actions.UpdateRequest import UpdateRequestActions

class UpdateRequest(UpdateRequestBase, UpdateRequestActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        UpdateRequestBase.__init__(self)
