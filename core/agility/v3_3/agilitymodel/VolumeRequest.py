from core.agility.v3_3.agilitymodel.base.VolumeRequest import VolumeRequestBase
from core.agility.v3_3.agilitymodel.actions.VolumeRequest import VolumeRequestActions

class VolumeRequest(VolumeRequestBase, VolumeRequestActions):
    '''
    classdocs
    '''
    def __init__(self, instance=None, operation=None, storage=[]):
        '''
        Constructor
        @param instance: instance minOccurs=0
        @type instance: Instance
        @param operation: operation
        @type operation: VolumeOperation
        @param storage: storage minOccurs=0 maxOccurs=unbounded
        @type storage: Link
        '''
        VolumeRequestBase.__init__(self, instance=instance, operation=operation, storage=storage)
