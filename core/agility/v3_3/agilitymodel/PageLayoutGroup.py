from core.agility.v3_3.agilitymodel.base.PageLayoutGroup import PageLayoutGroupBase
from core.agility.v3_3.agilitymodel.actions.PageLayoutGroup import PageLayoutGroupActions

class PageLayoutGroup(PageLayoutGroupBase, PageLayoutGroupActions):
    '''
    classdocs
    '''
    def __init__(self, name='', gridclass='', controls=[], description='', id=None, showheader=False, type=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param gridclass: gridclass
        @type gridclass: string
        @param controls: controls minOccurs=0 maxOccurs=unbounded
        @type controls: Control
        @param description: description
        @type description: string
        @param id: id
        @type id: int
        @param showheader: showheader
        @type showheader: boolean
        @param type: type
        @type type: string
        '''
        PageLayoutGroupBase.__init__(self, name=name, gridclass=gridclass, controls=controls, description=description, id=id, showheader=showheader, type=type)
