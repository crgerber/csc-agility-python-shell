from core.agility.v3_3.agilitymodel.base.PageLayout import PageLayoutBase
from core.agility.v3_3.agilitymodel.actions.PageLayout import PageLayoutActions

class PageLayout(PageLayoutBase, PageLayoutActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', groups=[], path='', description=''):
        '''
        Constructor
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: PageLayoutGroup
        @param path: path
        @type path: string
        @param description: description
        @type description: string
        '''
        PageLayoutBase.__init__(self, id=id, name=name, groups=groups, path=path, description=description)
