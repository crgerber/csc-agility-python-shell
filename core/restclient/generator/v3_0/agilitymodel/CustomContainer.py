from base.CustomContainer import CustomContainerBase
from actions.CustomContainer import CustomContainerActions

class CustomContainer(CustomContainerBase, CustomContainerActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        CustomContainerBase.__init__(self)
