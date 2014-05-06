from base.Stack import StackBase
from actions.Stack import StackActions

class Stack(StackBase, StackActions):
    '''
    classdocs
    '''
    def __init__(self, images=[], basestack=None, operatingsystem=None, template=None, targets=[]):
        '''
        Constructor
        @param images: images minOccurs=0 maxOccurs=unbounded
        @type images: Link
        @param basestack: basestack minOccurs=0
        @type basestack: Link
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param template: template minOccurs=0
        @type template: Link
        @param targets: targets minOccurs=0 maxOccurs=unbounded
        @type targets: Link
        '''
        StackBase.__init__(self, images=images, basestack=basestack, operatingsystem=operatingsystem, template=template, targets=targets)
