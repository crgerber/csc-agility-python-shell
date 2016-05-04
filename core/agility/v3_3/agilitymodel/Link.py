from base.Link import LinkBase
from actions.Link import LinkActions

class Link(LinkBase, LinkActions):
    '''
    classdocs
    '''
    def __init__(self, position=None, type='', id=None, rel='', linkproperty=[]):
        '''
        Constructor
        @param position: position minOccurs=0
        @type position: int
        @param type: type
        @type type: string
        @param id: id
        @type id: int
        @param rel: rel
        @type rel: string
        @param linkproperty: linkproperty minOccurs=0 maxOccurs=unbounded
        @type linkproperty: NameValuePair
        '''
        LinkBase.__init__(self, position=position, type=type, id=id, rel=rel, linkproperty=linkproperty)
