from core.agility.v3_3.agilitymodel.base.ItemLink import ItemLinkBase
from core.agility.v3_3.agilitymodel.actions.ItemLink import ItemLinkActions

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
