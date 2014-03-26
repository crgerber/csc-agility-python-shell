from core.agility.v3_0.agilitymodel.base.Link import LinkBase
from core.agility.v3_0.agilitymodel.actions.Link import LinkActions

class Link(LinkBase, LinkActions):
    '''
    classdocs
    '''
    def __init__(self, name='', linkproperty=[], href='', rel='', position=None, type='', id=None):
        '''
        Constructor
        @param name: name
        @type name: string
        @param linkproperty: linkproperty minOccurs=0 maxOccurs=unbounded
        @type linkproperty: NameValuePair
        @param href: href
        @type href: string
        @param rel: rel
        @type rel: string
        @param position: position minOccurs=0
        @type position: int
        @param type: type
        @type type: string
        @param id: id
        @type id: int
        '''
        LinkBase.__init__(self, name=name, linkproperty=linkproperty, href=href, rel=rel, position=position, type=type, id=id)
