from core.agility.v3_3.agilitymodel.base.Page import PageBase
from core.agility.v3_3.agilitymodel.actions.Page import PageActions

class Page(PageBase, PageActions):
    '''
    classdocs
    '''
    def __init__(self, selection=[], layout=None, users=[], title='', usergroups=[], context=None, menucategory=''):
        '''
        Constructor
        @param selection: selection minOccurs=0 maxOccurs=unbounded
        @type selection: AssetProperty
        @param layout: layout
        @type layout: PageLayout
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: int
        @param title: title
        @type title: string
        @param usergroups: usergroups minOccurs=0 maxOccurs=unbounded
        @type usergroups: int
        @param context: context
        @type context: PageContext
        @param menucategory: menucategory
        @type menucategory: string
        '''
        PageBase.__init__(self, selection=selection, layout=layout, users=users, title=title, usergroups=usergroups, context=context, menucategory=menucategory)
