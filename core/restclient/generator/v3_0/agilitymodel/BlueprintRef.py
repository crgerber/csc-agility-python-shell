from .base.BlueprintRef import BlueprintRefBase
from .actions.BlueprintRef import BlueprintRefActions

class BlueprintRef(BlueprintRefBase, BlueprintRefActions):
    '''
    classdocs
    '''
    def __init__(self, blueprint=None):
        '''
        Constructor
        @param blueprint: blueprint
        @type blueprint: Link
        '''
        BlueprintRefBase.__init__(self, blueprint=blueprint)
