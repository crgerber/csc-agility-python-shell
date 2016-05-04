from base.PageLayoutGroup import PageLayoutGroupBase
from actions.PageLayoutGroup import PageLayoutGroupActions

class PageLayoutGroup(PageLayoutGroupBase, PageLayoutGroupActions):
    '''
    classdocs
    '''
    def __init__(self, gridclass='', description='', showheader=False, controls=[], type='', id=None, name=''):
        '''
        Constructor
        @param gridclass: gridclass
        @type gridclass: string
        @param description: description
        @type description: string
        @param showheader: showheader
        @type showheader: boolean
        @param controls: controls minOccurs=0 maxOccurs=unbounded
        @type controls: Control
        @param type: type
        @type type: string
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        '''
        PageLayoutGroupBase.__init__(self, gridclass=gridclass, description=description, showheader=showheader, controls=controls, type=type, id=id, name=name)
