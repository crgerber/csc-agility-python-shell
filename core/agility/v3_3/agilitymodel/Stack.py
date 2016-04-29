from core.agility.v3_3.agilitymodel.base.Stack import StackBase
from core.agility.v3_3.agilitymodel.actions.Stack import StackActions

class Stack(StackBase, StackActions):
    '''
    classdocs
    '''
    def __init__(self, template=None, basestack=None, operatingsystem=None, targets=[], status=None, images=[]):
        '''
        Constructor
        @param template: template minOccurs=0
        @type template: Link
        @param basestack: basestack minOccurs=0
        @type basestack: Link
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param targets: targets minOccurs=0 maxOccurs=unbounded
        @type targets: Link
        @param status: status minOccurs=0
        @type status: string
        @param images: images minOccurs=0 maxOccurs=unbounded
        @type images: Link
        '''
        StackBase.__init__(self, template=template, basestack=basestack, operatingsystem=operatingsystem, targets=targets, status=status, images=images)
