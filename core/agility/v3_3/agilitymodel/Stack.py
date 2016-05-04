from base.Stack import StackBase
from actions.Stack import StackActions

class Stack(StackBase, StackActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, targets=[], template=None, images=[], basestack=None, operatingsystem=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param targets: targets minOccurs=0 maxOccurs=unbounded
        @type targets: Link
        @param template: template minOccurs=0
        @type template: Link
        @param images: images minOccurs=0 maxOccurs=unbounded
        @type images: Link
        @param basestack: basestack minOccurs=0
        @type basestack: Link
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        '''
        StackBase.__init__(self, status=status, targets=targets, template=template, images=images, basestack=basestack, operatingsystem=operatingsystem)
