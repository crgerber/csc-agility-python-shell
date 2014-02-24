from base.TargetCloud import TargetCloudBase
from actions.TargetCloud import TargetCloudActions

class TargetCloud(TargetCloudBase, TargetCloudActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, maxInstances=None, models=list(), template=None, stack=None, cloud=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param maxInstances: maxInstances minOccurs=0
        @type maxInstances: int
        @param models: models minOccurs=0 maxOccurs=unbounded
        @type models: Link
        @param template: template minOccurs=0
        @type template: Link
        @param stack: stack minOccurs=0
        @type stack: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        TargetCloudBase.__init__(self, status=status, maxInstances=maxInstances, models=models, template=template, stack=stack, cloud=cloud)
