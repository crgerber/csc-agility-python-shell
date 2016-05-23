from core.agility.v3_3.agilitymodel.base.PageContext import PageContextBase
from core.agility.v3_3.agilitymodel.actions.PageContext import PageContextActions

class PageContext(PageContextBase, PageContextActions):
    '''
    classdocs
    '''
    def __init__(self, name='', type='', description='', id=None, pagelinks=[], routes=[]):
        '''
        Constructor
        @param name: name
        @type name: string
        @param type: type
        @type type: string
        @param description: description
        @type description: string
        @param id: id
        @type id: int
        @param pagelinks: pagelinks minOccurs=0 maxOccurs=unbounded
        @type pagelinks: Link
        @param routes: routes minOccurs=0 maxOccurs=unbounded
        @type routes: AssetProperty
        '''
        PageContextBase.__init__(self, name=name, type=type, description=description, id=id, pagelinks=pagelinks, routes=routes)
