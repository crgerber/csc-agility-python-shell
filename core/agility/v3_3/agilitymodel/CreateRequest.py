from base.CreateRequest import CreateRequestBase
from actions.CreateRequest import CreateRequestActions

class CreateRequest(CreateRequestBase, CreateRequestActions):
    '''
    classdocs
    '''
    def __init__(self, asset=None, parent=None):
        '''
        Constructor
        @param asset: asset
        @type asset: Asset
        @param parent: parent minOccurs=0
        @type parent: Asset
        '''
        CreateRequestBase.__init__(self, asset=asset, parent=parent)
