from base.TargetCloud import TargetCloudBase
from actions.TargetCloud import TargetCloudActions

class TargetCloud(TargetCloudBase, TargetCloudActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, maxinstances=None, models=[], template=None, stack=None, cloud=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param maxinstances: maxinstances minOccurs=0
        @type maxinstances: int
        @param models: models minOccurs=0 maxOccurs=unbounded
        @type models: Link
        @param template: template minOccurs=0
        @type template: Link
        @param stack: stack minOccurs=0
        @type stack: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        TargetCloudBase.__init__(self, status=status, maxinstances=maxinstances, models=models, template=template, stack=stack, cloud=cloud)
