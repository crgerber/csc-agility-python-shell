from core.agility.v3_3.agilitymodel.base.TargetCloud import TargetCloudBase
from core.agility.v3_3.agilitymodel.actions.TargetCloud import TargetCloudActions

class TargetCloud(TargetCloudBase, TargetCloudActions):
    '''
    classdocs
    '''
    def __init__(self, template=None, cloud=None, stack=None, maxinstances=None, models=[], status=None):
        '''
        Constructor
        @param template: template minOccurs=0
        @type template: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param stack: stack minOccurs=0
        @type stack: Link
        @param maxinstances: maxinstances minOccurs=0
        @type maxinstances: int
        @param models: models minOccurs=0 maxOccurs=unbounded
        @type models: Link
        @param status: status minOccurs=0
        @type status: string
        '''
        TargetCloudBase.__init__(self, template=template, cloud=cloud, stack=stack, maxinstances=maxinstances, models=models, status=status)
