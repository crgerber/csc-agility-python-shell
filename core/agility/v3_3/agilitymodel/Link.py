from core.agility.v3_3.agilitymodel.base.Link import LinkBase
from core.agility.v3_3.agilitymodel.actions.Link import LinkActions

class Link(LinkBase, LinkActions):
    '''
    classdocs
    '''
    def __init__(self, linkproperty=[], position=None, rel='', id=None, type=''):
        '''
        Constructor
        @param linkproperty: linkproperty minOccurs=0 maxOccurs=unbounded
        @type linkproperty: NameValuePair
        @param position: position minOccurs=0
        @type position: int
        @param rel: rel
        @type rel: string
        @param id: id
        @type id: int
        @param type: type
        @type type: string
        '''
        LinkBase.__init__(self, linkproperty=linkproperty, position=position, rel=rel, id=id, type=type)
