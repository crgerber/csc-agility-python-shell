from core.agility.v3_3.agilitymodel.base.CustomContainerList import CustomContainerListBase
from core.agility.v3_3.agilitymodel.actions.CustomContainerList import CustomContainerListActions

class CustomContainerList(CustomContainerListBase, CustomContainerListActions):
    '''
    classdocs
    '''
    def __init__(self, customcontainer=[]):
        '''
        Constructor
        @param customcontainer: customcontainer minOccurs=0 maxOccurs=unbounded
        @type customcontainer: CustomContainer
        '''
        CustomContainerListBase.__init__(self, customcontainer=customcontainer)
