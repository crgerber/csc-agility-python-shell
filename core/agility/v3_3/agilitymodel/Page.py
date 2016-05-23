from core.agility.v3_3.agilitymodel.base.Page import PageBase
from core.agility.v3_3.agilitymodel.actions.Page import PageActions

class Page(PageBase, PageActions):
    '''
    classdocs
    '''
    def __init__(self, title='', context=None, selection=[], menucategory='', usergroups=[], layout=None, users=[]):
        '''
        Constructor
        @param title: title
        @type title: string
        @param context: context
        @type context: PageContext
        @param selection: selection minOccurs=0 maxOccurs=unbounded
        @type selection: AssetProperty
        @param menucategory: menucategory
        @type menucategory: string
        @param usergroups: usergroups minOccurs=0 maxOccurs=unbounded
        @type usergroups: int
        @param layout: layout
        @type layout: PageLayout
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: int
        '''
        PageBase.__init__(self, title=title, context=context, selection=selection, menucategory=menucategory, usergroups=usergroups, layout=layout, users=users)
