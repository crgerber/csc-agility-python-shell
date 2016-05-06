from core.agility.v3_3.agilitymodel.base.Linklist import LinklistBase
from core.agility.v3_3.agilitymodel.actions.Linklist import LinklistActions

class Linklist(LinklistBase, LinklistActions):
    '''
    classdocs
    '''
    def __init__(self, link=[]):
        '''
        Constructor
        @param link: link minOccurs=0 maxOccurs=unbounded
        @type link: Link
        '''
        LinklistBase.__init__(self, link=link)
