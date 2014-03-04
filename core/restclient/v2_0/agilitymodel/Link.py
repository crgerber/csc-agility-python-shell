from core.restclient.v2_0.agilitymodel.base.Link import LinkBase
from core.restclient.v2_0.agilitymodel.actions.Link import LinkActions

class Link(LinkBase, LinkActions):
    '''
    classdocs
    '''
    def __init__(self, name='', href='', rel='', position=None, type='', id=None):
        '''
        Constructor
        @param name: name
        @type name: string
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
        LinkBase.__init__(self, name=name, href=href, rel=rel, position=position, type=type, id=id)
