from core.agility.v3_3.agilitymodel.base.TargetCloud import TargetCloudBase
from core.agility.v3_3.agilitymodel.actions.TargetCloud import TargetCloudActions

class TargetCloud(TargetCloudBase, TargetCloudActions):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, models=[], template=None, stack=None, maxinstances=None, status=None):
        '''
        Constructor
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param models: models minOccurs=0 maxOccurs=unbounded
        @type models: Link
        @param template: template minOccurs=0
        @type template: Link
        @param stack: stack minOccurs=0
        @type stack: Link
        @param maxinstances: maxinstances minOccurs=0
        @type maxinstances: int
        @param status: status minOccurs=0
        @type status: string
        '''
        TargetCloudBase.__init__(self, cloud=cloud, models=models, template=template, stack=stack, maxinstances=maxinstances, status=status)
