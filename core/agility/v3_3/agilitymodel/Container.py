from core.agility.v3_3.agilitymodel.base.Container import ContainerBase
from core.agility.v3_3.agilitymodel.actions.Container import ContainerActions

class Container(ContainerBase, ContainerActions):
    '''
    classdocs
    '''
    def __init__(self, customcontainer=[], credential=[], package=[], blueprint=[], script=[], containerright=[], policy=[], project=[], container=[], stack=[], customitem=[], application=[]):
        '''
        Constructor
        @param customcontainer: customcontainer minOccurs=0 maxOccurs=unbounded
        @type customcontainer: Link
        @param credential: credential minOccurs=0 maxOccurs=unbounded
        @type credential: Link
        @param package: package minOccurs=0 maxOccurs=unbounded
        @type package: Link
        @param blueprint: blueprint minOccurs=0 maxOccurs=unbounded
        @type blueprint: Link
        @param script: script minOccurs=0 maxOccurs=unbounded
        @type script: Link
        @param containerright: containerright minOccurs=0 maxOccurs=unbounded
        @type containerright: Link
        @param policy: policy minOccurs=0 maxOccurs=unbounded
        @type policy: Link
        @param project: project minOccurs=0 maxOccurs=unbounded
        @type project: Link
        @param container: container minOccurs=0 maxOccurs=unbounded
        @type container: Link
        @param stack: stack minOccurs=0 maxOccurs=unbounded
        @type stack: Link
        @param customitem: customitem minOccurs=0 maxOccurs=unbounded
        @type customitem: Link
        @param application: application minOccurs=0 maxOccurs=unbounded
        @type application: Link
        '''
        ContainerBase.__init__(self, customcontainer=customcontainer, credential=credential, package=package, blueprint=blueprint, script=script, containerright=containerright, policy=policy, project=project, container=container, stack=stack, customitem=customitem, application=application)
