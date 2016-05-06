from core.agility.v3_3.agilitymodel.base.PageLayout import PageLayoutBase
from core.agility.v3_3.agilitymodel.actions.PageLayout import PageLayoutActions

class PageLayout(PageLayoutBase, PageLayoutActions):
    '''
    classdocs
    '''
    def __init__(self, path='', description='', id=None, groups=[], name=''):
        '''
        Constructor
        @param path: path
        @type path: string
        @param description: description
        @type description: string
        @param id: id
        @type id: int
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: PageLayoutGroup
        @param name: name
        @type name: string
        '''
        PageLayoutBase.__init__(self, path=path, description=description, id=id, groups=groups, name=name)
