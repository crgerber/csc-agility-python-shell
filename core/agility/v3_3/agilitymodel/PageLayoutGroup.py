from core.agility.v3_3.agilitymodel.base.PageLayoutGroup import PageLayoutGroupBase
from core.agility.v3_3.agilitymodel.actions.PageLayoutGroup import PageLayoutGroupActions

class PageLayoutGroup(PageLayoutGroupBase, PageLayoutGroupActions):
    '''
    classdocs
    '''
    def __init__(self, gridclass='', description='', controls=[], showheader=False, name='', id=None, type=''):
        '''
        Constructor
        @param gridclass: gridclass
        @type gridclass: string
        @param description: description
        @type description: string
        @param controls: controls minOccurs=0 maxOccurs=unbounded
        @type controls: Control
        @param showheader: showheader
        @type showheader: boolean
        @param name: name
        @type name: string
        @param id: id
        @type id: int
        @param type: type
        @type type: string
        '''
        PageLayoutGroupBase.__init__(self, gridclass=gridclass, description=description, controls=controls, showheader=showheader, name=name, id=id, type=type)
