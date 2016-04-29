from core.agility.v3_3.agilitymodel.base.PageLayout import PageLayoutBase
from core.agility.v3_3.agilitymodel.actions.PageLayout import PageLayoutActions

class PageLayout(PageLayoutBase, PageLayoutActions):
    '''
    classdocs
    '''
    def __init__(self, path='', groups=[], name='', description='', id=None):
        '''
        Constructor
        @param path: path
        @type path: string
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: PageLayoutGroup
        @param name: name
        @type name: string
        @param description: description
        @type description: string
        @param id: id
        @type id: int
        '''
        PageLayoutBase.__init__(self, path=path, groups=groups, name=name, description=description, id=id)
