from core.agility.v3_0.agilitymodel.base.Container import ContainerBase
from core.agility.v3_0.agilitymodel.actions.Container import ContainerActions

class Container(ContainerBase, ContainerActions):
    '''
    classdocs
    '''
    def __init__(self, blueprint=[], credential=[], container=[], package=[], script=[], customcontainer=[], customitem=[], containerright=[], project=[], application=[], policy=[], stack=[]):
        '''
        Constructor
        @param blueprint: blueprint minOccurs=0 maxOccurs=unbounded
        @type blueprint: Link
        @param credential: credential minOccurs=0 maxOccurs=unbounded
        @type credential: Link
        @param container: container minOccurs=0 maxOccurs=unbounded
        @type container: Link
        @param package: package minOccurs=0 maxOccurs=unbounded
        @type package: Link
        @param script: script minOccurs=0 maxOccurs=unbounded
        @type script: Link
        @param customcontainer: customcontainer minOccurs=0 maxOccurs=unbounded
        @type customcontainer: Link
        @param customitem: customitem minOccurs=0 maxOccurs=unbounded
        @type customitem: Link
        @param containerright: containerright minOccurs=0 maxOccurs=unbounded
        @type containerright: Link
        @param project: project minOccurs=0 maxOccurs=unbounded
        @type project: Link
        @param application: application minOccurs=0 maxOccurs=unbounded
        @type application: Link
        @param policy: policy minOccurs=0 maxOccurs=unbounded
        @type policy: Link
        @param stack: stack minOccurs=0 maxOccurs=unbounded
        @type stack: Link
        '''
        ContainerBase.__init__(self, blueprint=blueprint, credential=credential, container=container, package=package, script=script, customcontainer=customcontainer, customitem=customitem, containerright=containerright, project=project, application=application, policy=policy, stack=stack)
