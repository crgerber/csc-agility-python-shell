from core.agility.v2_0.agilitymodel.base.CustomContainer import CustomContainerBase
from core.agility.v2_0.agilitymodel.actions.CustomContainer import CustomContainerActions

class CustomContainer(CustomContainerBase, CustomContainerActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        CustomContainerBase.__init__(self)
