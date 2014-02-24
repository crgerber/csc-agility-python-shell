from base.Linklist import LinklistBase
from actions.Linklist import LinklistActions

class Linklist(LinklistBase, LinklistActions):
    '''
    classdocs
    '''
    def __init__(self, link=list()):
        '''
        Constructor
        @param link: link minOccurs=0 maxOccurs=unbounded
        @type link: Link
        '''
        LinklistBase.__init__(self, link=link)
