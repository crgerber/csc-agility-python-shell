from core.agility.v3_3.agilitymodel.base.GetMultipleRequest import GetMultipleRequestBase
from core.agility.v3_3.agilitymodel.actions.GetMultipleRequest import GetMultipleRequestActions

class GetMultipleRequest(GetMultipleRequestBase, GetMultipleRequestActions):
    '''
    classdocs
    '''
    def __init__(self, link=[]):
        '''
        Constructor
        @param link: link minOccurs=0 maxOccurs=unbounded
        @type link: Link
        '''
        GetMultipleRequestBase.__init__(self, link=link)
