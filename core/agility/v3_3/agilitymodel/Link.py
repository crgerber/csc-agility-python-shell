from core.agility.v3_3.agilitymodel.base.Link import LinkBase
from core.agility.v3_3.agilitymodel.actions.Link import LinkActions

class Link(LinkBase, LinkActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, rel='', position=None, linkproperty=[], type=''):
        '''
        Constructor
        @param id: id
        @type id: int
        @param rel: rel
        @type rel: string
        @param position: position minOccurs=0
        @type position: int
        @param linkproperty: linkproperty minOccurs=0 maxOccurs=unbounded
        @type linkproperty: NameValuePair
        @param type: type
        @type type: string
        '''
        LinkBase.__init__(self, id=id, rel=rel, position=position, linkproperty=linkproperty, type=type)
