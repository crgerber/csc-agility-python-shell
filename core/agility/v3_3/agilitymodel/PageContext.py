from core.agility.v3_3.agilitymodel.base.PageContext import PageContextBase
from core.agility.v3_3.agilitymodel.actions.PageContext import PageContextActions

class PageContext(PageContextBase, PageContextActions):
    '''
    classdocs
    '''
    def __init__(self, name='', description='', pagelinks=[], routes=[], id=None, type=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param description: description
        @type description: string
        @param pagelinks: pagelinks minOccurs=0 maxOccurs=unbounded
        @type pagelinks: Link
        @param routes: routes minOccurs=0 maxOccurs=unbounded
        @type routes: AssetProperty
        @param id: id
        @type id: int
        @param type: type
        @type type: string
        '''
        PageContextBase.__init__(self, name=name, description=description, pagelinks=pagelinks, routes=routes, id=id, type=type)
