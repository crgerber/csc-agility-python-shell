from core.agility.v2_0.agilitymodel.base.BlueprintRef import BlueprintRefBase
from core.agility.v2_0.agilitymodel.actions.BlueprintRef import BlueprintRefActions

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
