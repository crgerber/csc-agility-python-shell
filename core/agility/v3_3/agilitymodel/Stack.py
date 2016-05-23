from core.agility.v3_3.agilitymodel.base.Stack import StackBase
from core.agility.v3_3.agilitymodel.actions.Stack import StackActions

class Stack(StackBase, StackActions):
    '''
    classdocs
    '''
    def __init__(self, operatingsystem=None, status=None, template=None, images=[], basestack=None, targets=[]):
        '''
        Constructor
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param status: status minOccurs=0
        @type status: string
        @param template: template minOccurs=0
        @type template: Link
        @param images: images minOccurs=0 maxOccurs=unbounded
        @type images: Link
        @param basestack: basestack minOccurs=0
        @type basestack: Link
        @param targets: targets minOccurs=0 maxOccurs=unbounded
        @type targets: Link
        '''
        StackBase.__init__(self, operatingsystem=operatingsystem, status=status, template=template, images=images, basestack=basestack, targets=targets)
