from core.agility.v3_3.agilitymodel.base.PageContext import PageContextBase
from core.agility.v3_3.agilitymodel.actions.PageContext import PageContextActions

class PageContext(PageContextBase, PageContextActions):
    '''
    classdocs
    '''
    def __init__(self, description='', pagelinks=[], routes=[], type='', id=None, name=''):
        '''
        Constructor
        @param description: description
        @type description: string
        @param pagelinks: pagelinks minOccurs=0 maxOccurs=unbounded
        @type pagelinks: Link
        @param routes: routes minOccurs=0 maxOccurs=unbounded
        @type routes: AssetProperty
        @param type: type
        @type type: string
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        '''
        PageContextBase.__init__(self, description=description, pagelinks=pagelinks, routes=routes, type=type, id=id, name=name)
