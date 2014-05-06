from core.agility.v2_0.agilitymodel.base.Stack import StackBase
from core.agility.v2_0.agilitymodel.actions.Stack import StackActions

class Stack(StackBase, StackActions):
    '''
    classdocs
    '''
    def __init__(self, images=list(), baseStack=None, operatingSystem=None, template=None, targets=list()):
        '''
        Constructor
        @param images: images minOccurs=0 maxOccurs=unbounded
        @type images: Link
        @param baseStack: baseStack minOccurs=0
        @type baseStack: Link
        @param operatingSystem: operatingSystem minOccurs=0
        @type operatingSystem: string
        @param template: template minOccurs=0
        @type template: Link
        @param targets: targets minOccurs=0 maxOccurs=unbounded
        @type targets: Link
        '''
        StackBase.__init__(self, images=images, baseStack=baseStack, operatingSystem=operatingSystem, template=template, targets=targets)
