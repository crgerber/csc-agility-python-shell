from core.agility.v3_3.agilitymodel.base.Page import PageBase
from core.agility.v3_3.agilitymodel.actions.Page import PageActions

class Page(PageBase, PageActions):
    '''
    classdocs
    '''
    def __init__(self, menucategory='', context=None, users=[], title='', selection=[], usergroups=[], layout=None):
        '''
        Constructor
        @param menucategory: menucategory
        @type menucategory: string
        @param context: context
        @type context: PageContext
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: int
        @param title: title
        @type title: string
        @param selection: selection minOccurs=0 maxOccurs=unbounded
        @type selection: AssetProperty
        @param usergroups: usergroups minOccurs=0 maxOccurs=unbounded
        @type usergroups: int
        @param layout: layout
        @type layout: PageLayout
        '''
        PageBase.__init__(self, menucategory=menucategory, context=context, users=users, title=title, selection=selection, usergroups=usergroups, layout=layout)
