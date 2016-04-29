from .base.ItemLink import ItemLinkBase
from .actions.ItemLink import ItemLinkActions

class ItemLink(ItemLinkBase, ItemLinkActions):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        @param parent: parent minOccurs=0
        @type parent: Link
        '''
        ItemLinkBase.__init__(self, parent=parent)
