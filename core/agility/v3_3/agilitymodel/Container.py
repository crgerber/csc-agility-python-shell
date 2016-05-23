from core.agility.v3_3.agilitymodel.base.Container import ContainerBase
from core.agility.v3_3.agilitymodel.actions.Container import ContainerActions

class Container(ContainerBase, ContainerActions):
    '''
    classdocs
    '''
    def __init__(self, blueprint=[], stack=[], container=[], containerright=[], package=[], project=[], script=[], policy=[], customcontainer=[], customitem=[], application=[], credential=[]):
        '''
        Constructor
        @param blueprint: blueprint minOccurs=0 maxOccurs=unbounded
        @type blueprint: Link
        @param stack: stack minOccurs=0 maxOccurs=unbounded
        @type stack: Link
        @param container: container minOccurs=0 maxOccurs=unbounded
        @type container: Link
        @param containerright: containerright minOccurs=0 maxOccurs=unbounded
        @type containerright: Link
        @param package: package minOccurs=0 maxOccurs=unbounded
        @type package: Link
        @param project: project minOccurs=0 maxOccurs=unbounded
        @type project: Link
        @param script: script minOccurs=0 maxOccurs=unbounded
        @type script: Link
        @param policy: policy minOccurs=0 maxOccurs=unbounded
        @type policy: Link
        @param customcontainer: customcontainer minOccurs=0 maxOccurs=unbounded
        @type customcontainer: Link
        @param customitem: customitem minOccurs=0 maxOccurs=unbounded
        @type customitem: Link
        @param application: application minOccurs=0 maxOccurs=unbounded
        @type application: Link
        @param credential: credential minOccurs=0 maxOccurs=unbounded
        @type credential: Link
        '''
        ContainerBase.__init__(self, blueprint=blueprint, stack=stack, container=container, containerright=containerright, package=package, project=project, script=script, policy=policy, customcontainer=customcontainer, customitem=customitem, application=application, credential=credential)
